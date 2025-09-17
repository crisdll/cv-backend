from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExperienceViewSet, EducationViewSet, ProjectViewSet, SkillViewSet, ArticleViewSet

router = DefaultRouter()
router.register(r'experiences', ExperienceViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]