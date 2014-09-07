#!/usr/bin/python

import csv

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
    project_dict['project_id'] = row[0]
    project_dict['student_name'] = row[1]
    project_dict['project_name'] = row[2]
    project_dict['organization_name'] = row[3]
    status = row[4]
    assert(status == "accepted")
    project_dict['mentor_name'] = row[5]
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
