from django.contrib import admin
from .models import Module, Quiz, Challenge, SessionRecording

# Register your models here.
admin.site.register(Module)
admin.site.register(Quiz)
admin.site.register(Challenge)
admin.site.register(SessionRecording)