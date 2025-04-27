from django.shortcuts import render
from rest_framework import viewsets
from .models import Module, Quiz, Challenge, SessionRecording
from .serializers import ModuleSerializer, QuizSerializer, ChallengeSerializer, SessionRecordingSerializer

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class ChallengeViewSet(viewsets.ModelViewSet):
    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer

class SessionRecordingViewSet(viewsets.ModelViewSet):
    queryset = SessionRecording.objects.all()
    serializer_class = SessionRecordingSerializer


