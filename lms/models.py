# LMS (Learning Management System) models for managing modules, quizzes, challenges, and session recordings.
# This code defines the models for a Learning Management System (LMS) using Django ORM.
from django.db import models
from users.models import User

class Module(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Quiz(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    question = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)

class Challenge(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SessionRecording(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    tutor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    video = models.FileField(upload_to='recordings/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


