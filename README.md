# Pokedex (Django Backend)
Applicativo backend sviluppato in Django come esercizio: gestione di una lista di Pokémon salvata su database SQLite.

## Ambiente
- Windows + WSL Ubuntu
- VSCode (Remote - WSL)

## Requisiti
- Python 3
- Django


## Setup progetto

### 1 Clona il repository
    git clone https://github.com/branca-c/pokedex-django.git
    cd pokedex-django

### 2 Crea e attiva il virtualenv
    python3 -m venv venv
    source venv/bin/activate

### 3 Installa le dipendenze
    pip install django


## Database & Migrations
Esegui le migrations per creare il databse e la tabella dei Pokémon
    python manage.py makemigrations
    python manage.py migrate

## Avvio del server
    python manage.py runserver 0.0.0.0:8000

Apri da browser:
-  http://localhost:8000/pokemon/list


## API Endpoints
1) LIST - Lista Pokémon
   GET /pokemon/list

    Esempio:
    (bash)
    curl http://127.0.0.1:8000/pokemon/list

2) CREATE - Aggiunge un Pokémon
   POST /pokemon/

    Esempio:
    (bash)
    curl -X POST http://127.0.0.1:8000/pokemon/ \
        -H "Content-Type: application/json" \
        -d '{"name":"Pikachu","type1":"Electric","level":12,"hp":35}'

3) DELETE - Cancella un Pokémon (usando l'ID)
   POST /pokemon/delete

    Esempio:
    (bash)
    curl -X POST http://127.0.0.1:8000/pokemon/delete \
        -H "Content-Type: application/json" \
        -d '{"id": 1}'

NOTE:
Il DB utilizzato è SQLite (file db.sqlite3).
L'ID del Pokémon è generato automaticamente da Django ed è usato per la cancellazione.
Il virtualenv (venv/) è escluso dal repository tramite .gitignore.





