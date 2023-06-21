import secrets

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class user(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    security_question_1 = models.CharField(max_length=100)
    security_answer_1 = models.CharField(max_length=100)
    security_question_2 = models.CharField(max_length=100)
    security_answer_2 = models.CharField(max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'password']
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
