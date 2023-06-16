from django.forms import forms
from .models import user

class userForm(forms.ModelForm):
    class Meta:
        model=user
        fields = ["name","password","security_question_1","security_answer_1","security_question_2","security_answer_2"]