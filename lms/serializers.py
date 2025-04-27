from rest_framework import serializers
from .models import Module, Quiz, Challenge, SessionRecording

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'

class SessionRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionRecording
        fields = '__all__'
