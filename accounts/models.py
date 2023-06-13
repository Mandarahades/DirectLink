import secrets

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100, unique=True, default="NaN")
    password = models.CharField(max_length=50, default="NaN")
    security_question_1 = models.CharField(max_length=100, default="NaN")
    security_answer_1 = models.CharField(max_length=100, default="NaN")
    security_question_2 = models.CharField(max_length=100, default="NaN")
    security_answer_2 = models.CharField(max_length=100, default="NaN")
    photo = models.ImageField(upload_to='student', null=True, blank=True)
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['security_question_1', 'security_answer_1', 'security_question_2', 'security_answer_2']

    @property
    def is_authenticated(self):
        return True

    @property
    def is_anonymous(self):
        return False
    def clean_password(self):
        if len(self.password) < 8:
            raise ValidationError('Le mot de passe doit avoir au moins 8 caractères')


code = secrets.token_hex(2)
