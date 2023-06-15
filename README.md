# DirectLink

DirectLink est un projet qui permet de créer un module de profil d'utilisateur pour un site web avec question de sécurité. Ce module permet aux utilisateurs de s'inscrire, de se connecter, de modifier leurs informations personnelles et de réinitialiser leur mot de passe en répondant à une question de sécurité.

## Installation

Pour installer le projet, il faut cloner le dépôt Github et installer les dépendances avec la commande :

```bash
git clone https://github.com/MAG-ENCRYPTION/DirectLink.git
cd DirectLink
pip install -r requirements.txt
```

## Utilisation

Pour lancer le projet en local, il faut exécuter la commande :

```bash
python manage.py runserver
```

Le projet utilise SQLite comme base de données, il n'y a donc pas besoin de configurer quoi que ce soit.

Le projet utilise également le système d'authentification intégré à Django pour gérer les utilisateurs. Il faut donc créer un superutilisateur avec la commande :

```bash
python manage.py createsuperuser
```

## DEPLOIEMENT

Pour déployer DirectLink sur un serveur avec une API qu'une application pourra consommer, voici les étapes à suivre :

1. Assurez-vous que le serveur dispose d'un environnement Python 3.x et que les dépendances requises sont installées. Vous pouvez le faire en exécutant la commande `pip install -r requirements.txt` sur le serveur.
2. Créez une base de données pour le projet sur le serveur, de préférence en utilisant un système de base de données relationnelle tel que MySQL ou PostgreSQL.
3. Modifiez les paramètres de base de données dans le fichier `settings.py` en remplaçant les paramètres SQLite par ceux de votre système de base de données.
4. Créez un superutilisateur avec la commande `python manage.py createsuperuser`.
5. Déployez l'application sur le serveur en utilisant une méthode de votre choix, par exemple via FTP ou Git.
6. Exécutez la commande `python manage.py runserver` pour lancer l'application sur le serveur.
7. Exposez l'API de l'application à l'extérieur en utilisant une méthode telle que la configuration d'un proxy inversé ou l'utilisation de services tels que ngrok ou Heroku.
