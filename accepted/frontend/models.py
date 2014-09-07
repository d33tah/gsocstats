from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __repr__(self):
        return self.name

    __str__ = __repr__

class Organization(models.Model):
    name = models.CharField(max_length=255)

    def __repr__(self):
        return self.name

    __str__ = __repr__

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    student = models.ForeignKey('Person', related_name='worked_in')
    mentor = models.ForeignKey('Person', related_name='mentored')
    organization = models.ForeignKey('Organization')
    year = models.IntegerField()

    def __repr__(self):
        return self.name

    __str__ = __repr__
