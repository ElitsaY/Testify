from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student')
    )
    role = models.CharField(
        max_length = 10,
        choices = ROLE_CHOICES,
        #By default each new user is student
        default = 'student'
    )
    
    faculty_number = models.CharField(max_length = 10, unique = True, null = True, blank = True)
    
    def __str__(self):
        return f"{self.username} ({self.role})"