# Events-API
Project Overview

EventAPI is a Django REST Framework (DRF) application that allows users to register, create events, and purchase tickets with role-based access control (Admin & User). It uses JWT authentication for secure API access and integrates with PostgreSQL/MySQL as the database.

Installation & Setup :

1. Clone the Repository

git clone git@github.com:Aditya-Meena-26/Events-API.git
cd EventAPI

2. Create a Virtual Environment

python -m venv venv
# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Run Migrations

python manage.py makemigrations
python manage.py migrate

5. Create a Superuser (Admin Login)

python manage.py createsuperuser

6. Start the Django Server

python manage.py runserver

The API will be available at: http://127.0.0.1:8000/

7. Available Commands

Run the server: python manage.py runserver

Create migrations: python manage.py makemigrations

Apply migrations: python manage.py migrate

Create a superuser: python manage.py createsuperuser

Install dependencies: pip install -r requirements.txt