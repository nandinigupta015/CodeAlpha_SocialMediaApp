# Vibe — Social Media Platform

## CodeAlpha Full Stack Development Internship | Task 2

Vibe is a mini social media platform developed as part of the CodeAlpha Full Stack Development Internship.
It allows users to create posts with images, like and comment in real time, follow other users, and interact through a clean, modern, responsive UI.

This project demonstrates full-stack development skills using Django, JavaScript (AJAX), and modern UI design principles.

## 🚀 Features

User Authentication (Register / Login / Logout)

Create Posts (Text + Image Upload)

Global Feed (Reverse chronological order)

Like / Unlike Posts (AJAX-based, instant updates)

Comment on Posts (AJAX + real-time UI update)

Follow / Unfollow Users

User Profile Pages (Posts, Followers, Following)

Responsive Modern UI (Glassmorphism + Gradient theme)

## 🛠 Tech Stack
### Frontend

HTML

CSS

JavaScript (AJAX)

### Backend

Django (Python)

### Database

SQLite (Default Django database)

## 📂 Project Structure
CodeAlpha_SocialMediaApp/
│
├── core/
│   ├── migrations/
│   ├── static/core/
│   │   ├── style.css
│   │   └── main.js
│   ├── templates/core/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── profile.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── forms.py
│
├── socialsite/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt

## ⚙️ Setup & Installation
### 1️⃣ Clone the Repository
```
git clone https://github.com/nandinigupta015/CodeAlpha_SocialMediaApp.git
cd CodeAlpha_SocialMediaApp
```
### 2️⃣ Create & Activate Virtual Environment
```
python -m venv venv
```

Activate:

Windows:
```
venv\Scripts\activate
```

macOS / Linux:
```
source venv/bin/activate
```
### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```
### 4️⃣ Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
### 5️⃣ Run the Server
```
python manage.py runserver
```

### Open in browser:
👉 http://127.0.0.1:8000/

🔐 Dummy Users (For Testing)

The project includes a seed script to generate sample users and posts.

Run Seeder
```
python manage.py shell -c "from core.seed import run; run()"
```

Password for all dummy users:
```
12345678
```

Example Usernames:

sarahj

mikewav

cloudnine

alexzap

moonchild

### 📸 Screenshots

<img width="1920" height="785" alt="Screenshot (270)" src="https://github.com/user-attachments/assets/4de74036-8f8c-477e-af7a-488f403bf968" />


<img width="1920" height="821" alt="Screenshot (268)" src="https://github.com/user-attachments/assets/437225a9-4c78-4df2-8a7f-11b89e16a64c" />


<img width="1920" height="811" alt="Screenshot (269)" src="https://github.com/user-attachments/assets/d9886892-dbf6-4e4a-be28-e491db717edf" />


### 📚 Key Learnings

Django authentication & ORM

AJAX-based dynamic updates

Image upload handling

User relationship modeling (followers/following)

Full-stack integration & UI responsiveness

### 👩‍💻 Author

Nandini Gupta

B.Tech Computer Science & Engineering Student

GitHub: https://github.com/nandinigupta015/
