# 🏙️ Mini Divar API

A lightweight **classified ads backend** inspired by [Divar](https://divar.ir), built with **Django REST Framework**, **PostgreSQL**, **Redis**, **JWT**, and **Django Channels** for real-time chat.  

This backend includes **ads system**, **search & filters**, **pagination**, **user-owned ads**, and **private chat (conversations + messages)** between buyers and sellers.  
JWT authentication is implemented with **Redis** to manage sessions and tokens efficiently.

---

## 🚀 Features

| Feature | Explanation |
|------------|-------------|
| **🔐 Auth** | JWT-based authentication using Redis |
| **📝 Ads CRUD** | create + list + detail (slug based) + update/delete only by owner |
| **🗂 Categories & Cities** | choose category and city for every ad |
| **🔍 Search & Filter** | search by title + filter by category & city |
| **📄 Pagination** | custom pagination class |
| **💬 Chat System** | real-time chat between users implemented with Django Channels |
| **🕵️ Swagger** | API Docs with Swagger UI |

---

## ⚠️ Work in Progress

JWT authentication with Redis and real-time chat using Django Channels are currently under development and will be fully implemented soon.

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend** | Django, Django REST Framework, Django Channels |
| **Database** | PostgreSQL |
| **Cache / Message Broker** | Redis (used for JWT management & Channels) |
| **Containerization** | Docker, Docker Compose |
| **Auth** | JWT with Redis |
| **Pagination** | DRF built-in pagination |
| **Docs UI** | Swagger |

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
```
**Swagger Docs**
```bash
http://127.0.0.1:8000/swagger/
```
---
## 🧪 API Endpoints (Main)

### Ads
| Method | URL | Description |
|---|---|---|
| GET | `/api/v1/ads/` | List ads (Search + Filter + Pagination) |
| POST | `/api/v1/ads/` | Create new ad |
| GET | `/api/v1/ads/<slug>/` | Ad detail |
| GET | `/api/v1/my-ads/` | List ads just for logged-in user (only his/her ads) |

**Filtering examples**
```bash
/api/v1/ads/?search=laptop
/api/v1/ads/?category=3&city=2
```
### Conversations & Messages

| Method | URL | Description |
|---|---|---|
| GET / POST | `/api/v1/conversations/` | Create or list conversations |
| GET / POST | `/api/v1/conversations/<id>/messages/` | Send or list messages in a conversation |


---

## 🛠 Future Improvements (planned)

- Favorites / Bookmark ads

---

## 👤 Author

**Anita Masdoodi**  
Backend Developer — Django / DRF
