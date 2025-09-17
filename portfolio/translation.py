from modeltranslation.translator import register, TranslationOptions
from .models import Experience, Project, Skill, Education, Article

@register(Experience)
class ExperienceTranslationOptions(TranslationOptions):
    fields = ('company', 'position', 'key_words', 'short_description', 'description')

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'technologies', 'description')

@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('category', 'description')

@register(Education)
class EducationTranslationOptions(TranslationOptions):
    fields = ('institution', 'degree')

@register(Article)
class ArticleTranslationOptions(TranslationOptions):
    fields = ('title',)