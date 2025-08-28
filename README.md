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
