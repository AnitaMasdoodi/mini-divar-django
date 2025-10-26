# 🏙️ Mini Divar API

A lightweight **classified ads backend** inspired by [Divar](https://divar.ir), built with **Django REST Framework**, **PostgreSQL**, and **Docker**.  
This project focuses on creating a scalable and clean API for product listing, user management, and category-based browsing.

---

## 🚀 Features

- 🔐 JWT-based Authentication
- 👤 User registration & login
- 🗂️ Category-based ads
- 📦 CRUD operations for ads
- 🔍 Filtering & Pagination
- 🐘 PostgreSQL as database
- 🐳 Dockerized setup for easy deployment

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | Django, Django REST Framework |
| **Database** | PostgreSQL |
| **Containerization** | Docker, Docker Compose |
| **Auth** | JWT |
| **Pagination** | DRF built-in pagination |

---

## ⚙️ Setup Instructions

### 🐍 Local Development

```bash
git clone https://github.com/AnitaMasdoodi/mini-divar-django.git
cd mini-divar-django
python -m venv venv
source venv/bin/activate  # (on Windows: venv\Scripts\activate)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
