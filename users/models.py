from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_tutor = models.BooleanField(default=False)
    is_learner = models.BooleanField(default=True)
