import secrets

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    security_question_1 = models.CharField(max_length=100)
    security_answer_1 = models.CharField(max_length=100)
    security_question_2 = models.CharField(max_length=100)
    security_answer_2 = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='student', null=True, blank=True)

    def clean_password(self):
        if len(self.password) < 8:
            raise ValidationError('Le mot de passe doit avoir au moins 8 caractères')


code = secrets.token_hex(2)