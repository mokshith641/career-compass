from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):

    BRANCH_CHOICES = [
        ('CSE', 'Computer Science'),
        ('AIML', 'AI & Machine Learning'),
        ('IT', 'Information Technology'),
        ('ECE', 'Electronics & Communication'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES)

    skills = models.TextField()

    interests = models.TextField()

    def __str__(self):
        return self.user.username