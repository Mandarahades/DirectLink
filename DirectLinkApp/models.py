from django.db import models
from django.core.exceptions import ValidationError
import secrets


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    question1 = models.CharField(max_length=255)
    answer1 = models.CharField(max_length=255)
    question2 = models.CharField(max_length=255)
    answer2 = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='student', null=True, blank=True)

    def clean_password(self):
        if len(self.password) < 8:
            raise ValidationError('Le mot de passe doit avoir au moins 8 caractères')


code = secrets.token_hex(2)
