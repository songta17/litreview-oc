# Projet DA-Python - LitReview

## Initialisation du projet

### Récupération du projet

```
git clone git@github.com:songta17/litreview-oc.git
```

### Activation de l'environnement virtuel

```
cd litreview-oc
python -m venv env
source env/bin/activate
```

### Installation des paquets du projet

```
pip insstall -r requirements.txt
```

## Utilisation du projet

### Lancement du serveur

```
python manage.py runserver
```

### Ouverture du projet dans un navigateur

- Se rendre à l'adresse url locale http://127.0.0.1:8000/

## TODO

- [] système d'authentification et d'inscription
- [] créer un ticket pour demander des critiquess de livres ou d'articles
- [] publier des critiques de livres ou d'articles
- Sur la page du flux:
- [] voir ses reviews et ses tickets
- [] voir les reviews et tickets des personnes que l'user suit (follow)
- [] les avis en réponse à ses propres tickets
- [] créer seeds
- [] dans le readme, indiquer des logins utilisables pour les tests du client
- Intégration
- [] page d'accueil
- [] formulaire d'inscription
- [] flux
- [] onglet d'abonnements
- [] créer un ticket
- [] créer une critique (pas en réponse à un ticket)
- [] créer une critique (en réponses à un ticket)
- [] voir vos propress posts
- [] modifier votre propre critique
- [] modifier vore propre ticket
