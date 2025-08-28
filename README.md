# ✈️ TripLoop - Travel Booking Application (Django)

A simple web application for booking **Flights, Trains, and Buses**.  
Built with **Django** and deployed on **PythonAnywhere**.

---

## 🚀 Features
- **User Authentication**  
  - Register, login, logout  
  - Profile view and edit  

- **Travel Options**  
  - Browse available travel options (Flight, Train, Bus)  
  - Filter by type, source, destination, date  

- **Booking System**  
  - Book tickets by selecting a travel option  
  - Auto price calculation (seats × price)  
  - Prevents overbooking with validations & atomic transactions  
  - Cancel bookings (seats returned)  
  - View past & current bookings  

- **Admin Panel**  
  - Add, edit, and manage travel options  
  - Manage users and bookings  

---

## 🛠️ Tech Stack
- **Backend:** Python 3.10, Django 5  
- **Database:** MySQL (local + PythonAnywhere)  
- **Frontend:** Django templates, Bootstrap 5  
- **Deployment:** PythonAnywhere (Free Tier)  

---

## 🎯 Bonus Features Implemented
- ✅ MySQL as the database  
- ✅ Validation (seat availability, non-negative price)   
- ✅ Search & filtering (type, source, destination, date)  

---

## 📂 Project Structure
travel-booking-application/
│── booking/ # Main Django app
│ ├── migrations/
│ ├── templates/booking/ # HTML templates
│ │ ├── base.html
│ │ ├── book_ticket.html
│ │ ├── home.html
│ │ ├── login.html
│ │ ├── my_bookings.html
│ │ ├── profile_edit.html
│ │ ├── profile.html
│ │ ├── register.html
│ │ ├── travel_options.html
│ ├── admin.py
│ ├── forms.py
│ ├── models.py
│ └── tests.py
│ ├── urls.py
│ ├── views.py
│
│── travel_booking/ # Django project settings
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
│── staticfiles/ # Collected static files (after collectstatic)
│── manage.py
│── requirements.txt
│── README.md

---

## ⚡ Local Setup Instructions

### 1. Clone repo
```bash
git clone https://github.com/Ok-Ranjan/Travel-Booking-Application.git
cd travel-booking-application
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate     # (Linux/Mac)
venv\Scripts\activate        # (Windows)
source venv\Scripts\activate   # (bash)
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database (MYSQL)
Edit travel_booking/settings.py
```python
DATABASES = {
  'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'travel_db',
        'USER': 'root',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Collect Static Files
```bash
python manage.py collectstatic
```

### 8. Run Development Server
```bash
python manage.py runserver
```
Visit -> http://127.0.0.1:8000/

# ☁️ Deployment on PythonAnywhere
### 1. Push Code to GitHub
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/travel-booking-application.git
git push -u origin master
```

### 2. On PythonAnywhere
-> Open a Bash console
-> Clone repo:
  ```bash
  git clone https://github.com/yourusername/travel-booking-application.git
  cd travel-booking-application
  ```

### 3. Virtual Environment
```bash
mkvirtualenv --python=/usr/bin/python3.10 travelenv
pip install -r requirements.txt
```

### 4. Create MySQL Database
From Databases tab:
-> Database name: yourusername$travel_db
-> Host: yourusername.mysql.pythonanywhere-services.com

Update settings.py with these values:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$travel_db',
        'USER': 'yourusername',
        'PASSWORD': 'YourPasswordHere',
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}
```

Run:
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 5. Static Files
```bash
python manage.py collectstatic
```

In Web tab -> Static files:
-> URL: /static/
-> Path: /home/yourusername/travel-booking/staticfiles

### 6. Configure Web App
-> Web tab → Add new web app → Manual config (Python 3.10)
-> Set virtualenv path: /home/yourusername/.virtualenvs/travelenv
-> Edit WSGI configuration file:
1. click on link
2. Edit:
```python
import os, sys
path = '/home/yourusername/travel-booking'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_booking.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

-> Reload app
[Your app is live at](https://yourusername.pythonanywhere.com):

# 👨‍💻 Author
### Ranjan Kumar
B.Tech (CSE), Millennium Institute of Technology and Science, Bhopal
Passionate about problem-solving, web development, and AI 🚀

# 📜 License
MIT License — free to use and modify.
