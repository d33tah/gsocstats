#!/usr/bin/python

import csv
from lxml import html

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "frontend.settings")
from frontend.models import Person, Organization, Project
from django.db import transaction
from django.utils.encoding import smart_str as s

by_student = {}
by_project = {}
by_mentor = {}
by_organization = {}
by_year = {}

def add_to_dict(dict_, key, project_dict):
    if not key in dict_:
        dict_[key] = [project_dict]
    else:
        dict_[key] += [project_dict]

def parse_row(row, year):
    global by_student, by_project, by_mentor, by_organization, by_year
    project_dict = {}
    project_dict['year'] = year
    project_dict['project_id'] = s(row[0])
    project_dict['student_name'] = s(row[1])
    project_dict['project_name'] = s(row[2])
    project_dict['organization_name'] = s(row[3])
    status = s(row[4])
    assert(status == "accepted")
    project_dict['mentor_name'] = s(row[5])
    add_to_dict(by_student, project_dict['student_name'], project_dict)
    add_to_dict(by_mentor, project_dict['mentor_name'], project_dict)
    add_to_dict(by_project, project_dict['project_name'], project_dict)
    add_to_dict(by_organization, project_dict['organization_name'], project_dict)
    add_to_dict(by_year, year, project_dict)

for year in range(2009,2014):
    with open("%s.csv" % year) as csvfile:
        r = csv.reader(csvfile)
        skipped = False
        for row in r:
            if not skipped:
                skipped = True
            else:
                parse_row(row, year)

for year in range(2005, 2009):
    t = html.parse("%d.html" % year)
    for organization_h2 in t.xpath("//section/h2"):
        organization_name = organization_h2.text_content()
        for project_h2 in organization_h2.xpath("../ul/li"):
            project_name = project_h2[0].text_content()
            project_tail = project_h2[0].tail.lstrip().rstrip()[3:]
            student_name, mentor_name = project_tail.split(', mentored by ')

            project_dict = {}
            project_dict['year'] = year
            #project_dict['project_id'] = row[0]
            project_dict['student_name'] = s(student_name.strip())
            project_dict['project_name'] = s(project_name)
            project_dict['organization_name'] = s(organization_name)
            #status = row[4]
            #assert(status == "accepted")
            project_dict['mentor_name'] = s(mentor_name.strip())
            add_to_dict(by_student, project_dict['student_name'], project_dict)
            add_to_dict(by_mentor, project_dict['mentor_name'], project_dict)
            add_to_dict(by_project, project_dict['project_name'], project_dict)
            add_to_dict(by_organization, project_dict['organization_name'], project_dict)
            add_to_dict(by_year, year, project_dict)

transaction.set_autocommit(False)

people = {x for x in by_mentor}.union({x for x in by_student})
people_objs = {}
for person in people:
    o = Person(name=person)
    o.save()
    people_objs[person] = o

organization_objs = {}
for organization in by_organization:
    o = Organization(name=organization)
    o.save()
    organization_objs[organization] = o

for project_list in by_project.values():
    project = project_list[0]
    student = people_objs[project['student_name']]
    mentor = people_objs[project['mentor_name']]
    year = int(project['year'])
    name = project['project_name']
    organization = organization_objs[project['organization_name']]
    o = Project(student=student, mentor=mentor, year=year, name=name,
                organization=organization)
    o.save()

transaction.set_autocommit(True)
