from django.contrib import admin
from frontend.models import Person, Organization, Project

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', )
admin.site.register(Person, PersonAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list
admin.site.register(Organization, OrganizationAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'student', 'mentor', 'year')
    search_fields = ['name', 'organization__name', 'student__name', 'mentor__name', 'year']
    list_filter = ('year',)
    pass
admin.site.register(Project, ProjectAdmin)
