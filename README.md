# Event Management

**Event Management** is a Django REST API application for managing events (conferences, meetups, etc.).  
The API allows you to create, view, update, and delete events, as well as register users for those events.  
It supports user authentication, email notifications, and containerization via Docker.

## 🔧 Features

- CRUD operations for the Event model
- User registration and authentication
- User registration for events
- Email confirmation after successful event registration
- API documentation
- Dockerfile for containerized deployment

## 🧱 Technologies

- Python
- Django / Django REST Framework
- SQLite 
- Docker
- Swagger or DRF Spectacular for API documentation

## ⚙️ Installation

```bash
git clone https://github.com/Julia-ms3/EventManagement.git
cd EventManagement

# ▶️ Run with Docker
docker build -t event-app .
docker run -it --rm -p 8000:8000 event-app

# ▶️ Local run without Docker (make sure Python 3.10+ and pip are installed)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate for Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


#Authentication

TokenAuthentication is used.
Standard user registration and login endpoints are implemented.

#Email Notifications

Users receive a confirmation email after registering for an event.
SMTP server configuration is used for sending emails.

# API Documentation

Once the server is running, the API documentation is available at:

OpenAPI schema: http://localhost:8000/api/schema/
Swagger UI or Redoc: http://localhost:8000/api/docs/
