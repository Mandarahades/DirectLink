from django.shortcuts import *
from django.contrib.auth import *

from DirectLinkApp.models import Student


def signup(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
    if len(password) < 8:
        context = {'error': 'Mot de passe insuffisant'}
        return render(request, 'registration/signup.html', context)
    question1 = request.POST['question1']
    answer1 = request.POST['answer1']
    question2 = request.POST['question2']
    answer2 = request.POST['answer2']
    student = Student(name=name, email=email, password=password,
                      security_question1=question1, security_answer1=answer1,
                      security_question2=question2, security_answer2=answer2)
    student.save()
    return render(request, 'registration/profile.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            student = Student.objects.get(email=email)
            if student.password == password:
                request.session['email'] = email
                return redirect('profile')
            else:
                context = {'error': 'Mot de passe incorrect'}
                return render(request, 'registration/login.html', context)
        except Student.DoesNotExist:
            context = {'error': 'Utilisateur inexistant'}
            return render(request, 'registration/login.html', context)
    else:
        return render(request, 'registration/login.html')


def profile(request):
    email = request.session['email']
    student = Student.objects.get(email=email)
    if request.method == 'POST':
        question1 = request.POST['question1']
        answer1 = request.POST['answer1']
        question2 = request.POST['question2']
        answer2 = request.POST['answer2']
        if question1 == student.security_question1 and \
                answer1 == student.security_answer1 and \
                question2 == student.security_question2 and \
                answer2 == student.security_answer2:
            return render(request, 'registration/new_password.html')
        else:
            context = {'error': 'Réponses aux questions de sécurité incorrectes'}
            return render(request, 'registration/profile.html', context)
    return render(request, 'registration/profile.html')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            student = Student.objects.get(email=email)
            code = randint(1000,9999)
            # Envoie un email avec le code
            return render(request, 'registration/code.html', {'code':code})
        except Student.DoesNotExist:
            context = {'error': 'Adresse email inexistante'}
            return render(request, 'registration/forgot_password.html', context)
    return render(request, 'registration/forgot_password.html')


def check_code(request):
    if request.method == 'POST':
        code = request.POST['code']
        if code == request.session['code']:
            return render(request, 'registration/new_password.html')
        else:
            context = {'error': 'Code incorrect'}
            return render(request, 'registration/code.html', context)
    return render(request, 'registration/code.html')

def index(request):
    return render(request,'accounts/index.html')
def index2(request):
    return render(request,'accounts/forgotten.html')
def index3(request):
    return render(request,'accounts/SecuredQuestions.html')
def index4(request):
    return render(request,'accounts/reload.html')
