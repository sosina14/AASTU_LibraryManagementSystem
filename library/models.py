from django.contrib.auth.models import AbstractUser
from django.db import models

# User Roles
ROLE_CHOICES = (
    ('student', 'Student'),
    ('admin', 'Admin'),
    ('superadmin', 'Super Admin'),
)

class CustomUser(AbstractUser):
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    def __str__(self):
        return f"{self.username} ({self.role})"


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    available_copies = models.IntegerField(default=1)
    
    def __str__(self):
        return self.title
