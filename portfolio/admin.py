from django.contrib import admin
from .models import Project, Skill, Experience, Education



@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'start_date', 'end_date','key_words','description')
    list_filter = ('company', 'start_date','end_date')
    search_fields = ('company', 'position','key_words')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'technologies', 'url','description')
    search_fields = ('title', 'technologies')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'proficiency')
    list_filter = ('category', 'proficiency')
    search_fields = ('name',)

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'degree', 'start_date', 'end_date')
    list_filter = ('institution', 'start_date')
    search_fields = ('institution', 'degree')