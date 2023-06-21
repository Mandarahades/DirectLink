from base64 import urlsafe_b64encode, urlsafe_b64decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator

from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth import login, authenticate

def home(request):
    return render(request, 'accounts/index.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        security_question_1 = request.POST.get('security_question_1')
        security_answer_1 = request.POST.get('security_answer_1')
        security_question_2 = request.POST.get('security_question_2')
        security_answer_2 = request.POST.get('security_answer_2')

        # Create a new user object
        user = user(
            username=username,
            password=password,
            security_question_1=security_question_1,
            security_answer_1=security_answer_1,
            security_question_2=security_question_2,
            security_answer_2=security_answer_2
        )
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        # Get the form data from the request
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})
    else:
        return render(request, 'accounts/login.html')

def password_reset(request):
    if request.method == 'GET':
        return render(request, 'accounts/password_reset.html', {'form': PasswordResetForm()})
    else:
        # Récupération des données du formulaire
        username = request.POST.get('username')
        try:
            user = user.objects.get(username=username)
        except user.DoesNotExist:
            # Si l'utilisateur n'existe pas, on affiche un message d'erreur
            return render(request, 'accounts/password_reset.html', {'form': PasswordResetForm(), 'error_message': 'Nom d\'utilisateur invalide'})
        # Vérification des réponses aux questions de sécurité
        security_answer_1 = request.POST.get('security_answer_1')
        security_answer_2 = request.POST.get('security_answer_2')
        if user.security_answer_1 != security_answer_1 or user.security_answer_2 != security_answer_2:
            # Si les réponses ne correspondent pas, on affiche un message d'erreur et on vide les champs
            return render(request, 'accounts/password_reset.html',{'error_message': 'Réponses aux questions de sécurité incorrectes', 'username': username})
        else:
            # Si les réponses sont correctes, on redirige l'utilisateur vers la page de réinitialisation du mot de passe
            return redirect('password_reset_confirm', uidb64=urlsafe_b64encode(force_bytes(user.pk)).decode(), token=default_token_generator.make_token(user))
        
def reset_password_confirm(request, uidb64, token):
    try:
        # Décodage de l'ID utilisateur et vérification du jeton de réinitialisation de mot de passe
        uid = force_str(urlsafe_b64decode(uidb64))
        user = user.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            # Utilisation du formulaire SetPasswordForm pour permettre à l'utilisateur de saisir un nouveau mot de passe
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
        else:
            form = SetPasswordForm(user)
        return render(request, 'accounts/reset_password_confirm.html', {'form': form})
    else:
        return redirect('home')