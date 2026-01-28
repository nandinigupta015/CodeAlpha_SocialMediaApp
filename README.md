# ✨ Vibe — Social Media Platform (CodeAlpha Internship Task)

Vibe is a mini social media platform built as part of the **CodeAlpha Full Stack Development Internship (Task 2)**.  
It allows users to create posts, upload images, like posts, comment in real-time, and follow other users — all inside a clean modern UI.

---

## 🚀 Features

✅ User Authentication (Register / Login / Logout)  
✅ Create Post (Text + Image Upload)  
✅ View Feed (All posts in reverse chronological order)  
✅ Like / Unlike Posts (AJAX)  
✅ Comment on Posts (AJAX + instant UI update)  
✅ Follow / Unfollow Users  
✅ User Profile Page (Posts + Followers + Following stats)  
✅ Responsive Modern UI (Glassmorphism + Gradient Theme)

---

## 🛠 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Django (Python)

### Database
- SQLite (Default Django DB)

---

## 📂 Project Structure

```txt
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
```
### ⚙️ Setup & Installation

✅ 1. Clone the Repository
```
git clone https://github.com/nandinigupta015/CodeAlpha_SocialMediaApp.git
cd CodeAlpha_SocialMediaApp
```
✅ 2. Create Virtual Environment
```
python -m venv venv
```

Activate it:

Windows
```
venv\Scripts\activate
```

Mac/Linux
```
source venv/bin/activate
```
✅ 3. Install Dependencies
```
pip install -r requirements.txt
```
✅ 4. Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```
✅ 5. Run the Project
```
python manage.py runserver
```

Open in browser:
👉 http://127.0.0.1:8000/

🔐 Dummy Users (For Testing)

The project includes a seed script to generate dummy accounts & posts.

✅ Run Seeder
```
python manage.py shell -c "from core.seed import run; run()"
```

✅ Password for all dummy users:
```
12345678
```

Example usernames:

sarahj

mikewav

cloudnine

alexzap

moonchild

👩‍💻 Author

Nandini Gupta
B.Tech CSE Student
GitHub: https://github.com/nandinigupta015/


---
