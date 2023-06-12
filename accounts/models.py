import secrets

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class Student(AbstractUser):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    security_question_1 = models.CharField(max_length=100)
    security_answer_1 = models.CharField(max_length=100)
    security_question_2 = models.CharField(max_length=100)
    security_answer_2 = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='student', null=True, blank=True)
    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email', 'security_question_1', 'security_answer_1', 'security_question_2', 'security_answer_2']

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
