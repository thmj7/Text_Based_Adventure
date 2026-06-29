# Text_Based_Adventure
Mysterious Forest is a Django-based text adventure game where player choices drive a branching story with multiple paths and endings. Scenes and choices are managed through the Django Admin panel, allowing the narrative to be expanded without changing code.

# 🌲 Mysterious Forest – Django Text Adventure

An interactive text-based adventure game inspired by branching narrative games like *Elmwood Trail*.

## Features
- Branching story logic using Django models
- Admin-controlled scenes and choices
- Atmospheric forest background
- Multiple endings

## Tech Stack
- Python
- Django
- HTML / CSS
- SQLite (development)

## Setup Instructions

```bash
git clone https://github.com/yourusername/django-text-adventure.git
cd django-text-adventure
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
