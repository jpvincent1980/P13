> ## Statut CircleCI
> #### (développement -> branche "develop")

[![CircleCI](https://circleci.com/gh/jpvincent1980/P13/tree/develop.svg?style=svg)](https://circleci.com/gh/jpvincent1980/P13/tree/main)

> ## Résumé

Site web d'Orange County Lettings

> ## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/jpvincent1980/P13.git`

#### Créer l'environnement virtuel

- `cd /path/to/P13`
- `python -m venv env`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source env/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/P13`
- `source env/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/P13`
- `source env/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/P13`
- `source env/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/P13`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(P13_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\env\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Créer manuellement un conteneur Docker de l'application

L'application nécessite l'utilisation de variables d'environnement.  

Ces variables d'environnement seront enregistrées dans un fichier nommé `.env` qui sera utilisé lors de la création du conteneur Docker.  

Créez un fichier `.env` contenant les variables d'environnement ci-dessous:

**SECRET_KEY**=*Votre clé secrète Django*  
**DEBUG**=True  
**ALLOWED_HOSTS**=127.0.0.1,localhost,*nomdevotreapplication.herokuapp.com*  
**SENTRY_DSN**=*Le DSN Sentry de votre application.*

Les valeurs sont à renseigner sans être entourées par " " ou ' '.

Indiquez l'utilisation des variables d'environnement contenues dans ce fichier lors de la création du conteneur Docker en saisissant la commande ci-dessous depuis votre terminal:

`docker run -d -p 8000:8000 --env-file /path/to/.env/file/.env <nomdevotreimageDocker>`

### Envoyer manuellement l'image Docker de l'application sur Docker Hub

Connectez-vous à votre compte Docker Hub depuis votre terminal en saisissant la commande ci-dessous:

- Sous Windows -> `winpty docker login -u <votrelogin>`

- Sous Mac/Linux -> `docker login -u <votrelogin>`

Saisissez votre mot de passe Docker Hub lorsqu'il vous sera demandé.

Une fois votre terminal connecté, saisissez la commande ci-dessous:

`docker push <nomdevotreimageDocker>`

Un repository est alors créé sur votre compte Docker Hub contenant votre image Docker. Ce repository est accessible à l'adresse ci-dessous:

`https://hub.docker.com/repository/docker/<votreloginDockerHub>/<nomdevotreimageDocker>`

### Déployer manuellement l'application sur Heroku

Dans votre terminal, placez-vous dans le répertoire de l'application et saisissez la commande ci-dessous:

`git push heroku main`  


> ## Déploiement

### Fonctionnement du déploiement

Le déploiement de l'application OC-lettings se fait via un pipeline CI/CD sur CircleCI qui exécute l'application, l'englobe dans un container Docker qui est ensuite déployé sur Heroku.

### Configuration requise au déploiement

### Installations

* #### Installation de Docker

Installez Docker sur votre poste en suivant les instructions au lien ci-dessous:

https://docs.docker.com/get-docker/

*  #### Installation d'Heroku

Installez Heroku sur votre poste en suivant les instructions au lien ci-dessous:

https://devcenter.heroku.com/articles/heroku-cli#install-the-heroku-cli

### Inscriptions

  * #### Compte CircleCI

Il est nécessaire de se connecter sur le site CircleCi à l'adresse suivante afin de pouvoir surveiller la progression du pipeline CI/CD et y apporter des modifications si nécessaire:

https://circleci.com/login/

Si vous ne disposez pas d'un compte CircleCI, inscrivez-vous à l'adresse suivante en choisissant *Sign Up with GitHub* afin que vos comptes CircleCI et GitHub soient directement liés :

https://circleci.com/signup/

Si votre compte CircleCi n'est pas lié à votre compte GitHub, allez dans *User Settings* à l'adresse ci-dessous et cliquez sur le bouton *Connect* de l'onglet GitHub:

https://app.circleci.com/settings/user

Une fois vos comptes CircleCi et GitHub liés, cliquez sur *Projects* dans la barre de navigation CircleCI, cherchez le dépôt GitHub de l'application parmi tous ceux de votre compte GitHub et cliquez sur *Set Up Project*.

Votre projet CircleCI est créé. Cliquez sur son nom afin de le paramétrer.

Les variables d'environnement de votre projet CircleCI sont paramétrables dans *Project Settings* -> *Environment Variables* et sont les suivantes:

**SECRET_KEY** = Votre clé secrète Django.  
**ALLOWED_HOSTS** = 127.0.0.1,localhost,*nomdevotreapplication.herokuapp.com*  
**DOCKER_LOGIN** = Le login de votre compte Docker Hub sur lequel l'image de l'application est envoyée.  
**DOCKER_PASSWORD** = Le mot de passe de votre compte Docker Hub sur lequel l'image de l'application est envoyée.  
**HEROKU_API_KEY** = La clé API de votre compte Heroku sur lequel l'application est déployée.  
**HEROKU_APP_NAME** = Le nom de votre application Heroku.   
**SENTRY_DSN** = Le DSN Sentry de votre application.  

* #### Compte Docker Hub

Si vous ne disposez pas d'un compte Docker Hub, inscrivez-vous à l'adresse suivante:

https://hub.docker.com/signup

Pour vous connecter à votre compte Docker Hub, rendez-vous au lien ci-dessous:

https://login.docker.com/u/login

Allez renseigner votre login et votre mot de passe Docker Hub dans les variables d'environnement de votre projet CircleCI avec respectivement les clés **DOCKER_LOGIN** et **DOCKER_PASSWORD**.  

* #### Compte Heroku

Si vous ne disposez pas d'un compte Heroku, inscrivez-vous à l'adresse suivante:

https://signup.heroku.com/

Pour vous connecter à votre compte Heroku, rendez-vous au lien ci-dessous:

https://id.heroku.com/

Sur votre tableau de bord Heroku, cliquez sur *New* puis *Create new app*.

Choisissez un nom d'application disponible, sélectionnez votre région (Europe) et cliquez sur *Create app*.

Une fois votre application créée, sélectionnez-la dans votre tableau de bord puis définissez ses variables d'environnement en cliquant sur l'onglet *Settings*, puis *Reveal Config Vars*:

**SECRET_KEY** = Votre clé secrète Django.  
**ALLOWED_HOSTS** = 127.0.0.1,localhost,*nomdevotreapplication.herokuapp.com*   
**SENTRY_DSN** = Le DSN Sentry de votre application. 

Récupérez votre clé API en allant dans les paramètres de votre compte utilisateur Heroku -> *Account settings* puis *API key*.

Allez renseigner votre clé API et votre nom d'application Heroku dans les variables d'environnement de votre projet CircleCI, respectivement avec les clés **HEROKU_API_KEY** et **HEROKU_APP_NAME**.

* #### Compte Sentry

Si vous ne disposez pas d'un compte Sentry, inscrivez-vous à l'adresse suivante:

https://sentry.io/signup/

Pour vous connecter à votre compte Sentry, rendez-vous au lien ci-dessous:

https://sentry.io/auth/login/

Une fois connecté(e) à votre compte Sentry, cliquez sur *Create Project*, choisissez Django comme plateforme et donnez un nom à votre projet.

Une fois votre projet créé, sélectionnez-le, cliquez sur *Settings*, puis dans la rubrique *SDK Setup*, cliquez sur *Client Keys (DSN)* et récupérez votre DSN à renseigner dans les variables d'environnement sur CircleCI et Heroku (avec pour clé **SENTRY_DSN** dans les deux cas).  

### Etapes nécessaires pour effectuer le déploiement

La première étape du déploiement est l'envoi d'un pull request sur la branche main du dépôt GitHub.

Ce pull request va déclencher le démarrage d'un pipeline sur le projet CircleCi lié au dépôt GitHub.

La première étape du pipeline est le build de l'application.

Si le build échoue, les prochaines étapes ne sont pas effectuées.

En cas de succès, les étapes de linting et de test sont alors lancées concamitamment.

Si le linting ou les tests échouent, les prochianes étapes ne sont pas effectuées.

En cas de succès, un container Docker englobant l'application est créé conformément à l'image Docker et aux directives présentes dans le fichier Dockerfile du projet.

Si la conteneurisation échoue, la prochaine et dernière étape n'est pas effectuée.

En cas de succès, le conteneur englobant l'application est déployé sur Heroku et la nouvelle version de celle-ci est disponible à l'adresse ci-dessous:

`oc-lettings-jpvincent.herokuapp.com`

Test