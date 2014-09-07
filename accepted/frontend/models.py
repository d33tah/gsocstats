from django.db import models
from django.utils.encoding import smart_str

class Person(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return smart_str(self.name)

    __str__ = __repr__

class Organization(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return smart_str(self.name)

    __str__ = __repr__

class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)
    student = models.ForeignKey('Person', related_name='worked_in')
    mentor = models.ForeignKey('Person', related_name='mentored')
    organization = models.ForeignKey('Organization')
    year = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __repr__(self):
        return smart_str(self.name)

    __str__ = __repr__
