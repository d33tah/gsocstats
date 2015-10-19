from django.contrib import admin
from frontend.models import Person, Organization, Project

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']
admin.site.register(Person, PersonAdmin)

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ['name']
admin.site.register(Organization, OrganizationAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'student', 'mentor', 'year')
    search_fields = ['name', 'organization__name', 'student__name', 'mentor__name', 'year']
    list_filter = ('year',)

    def lookup_allowed(self, key, value):
        if key in ('organization__name'):
            return True
        return super(ProjectAdmin, self).lookup_allowed(key, value)

admin.site.register(Project, ProjectAdmin)
