from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ModuleViewSet, QuizViewSet, ChallengeViewSet, SessionRecordingViewSet

router = DefaultRouter()
router.register(r'modules', ModuleViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'challenges', ChallengeViewSet)
router.register(r'sessions', SessionRecordingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
# This code defines the URL routing for the LMS (Learning Management System) application. It uses Django's DefaultRouter to automatically generate the URL patterns for the viewsets defined in the views.py file. The urlpatterns list includes paths for modules, quizzes, challenges, and session recordings, allowing for easy access to these resources via RESTful API endpoints.
