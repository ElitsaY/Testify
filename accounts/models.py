from django.db import models
from django.contrib.auth.models import AbstractUser

class Student(AbstractUser):
    faculty_number = models.CharField(max_length = 10, unique = True, null = False, blank = False)

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    
    def __str__(self):
        return self.username