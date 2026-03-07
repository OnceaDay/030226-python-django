
# We ♥ Anime — Django CRUD Application

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Django](https://img.shields.io/badge/Django-Framework-green)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey)
![License](https://img.shields.io/badge/License-Educational-blue)

A **Django-based CRUD web application** for managing a personal anime catalog.

The application allows users to:

- Add anime entries
- Edit existing entries
- Delete records
- View stored anime information

This project demonstrates core **Django development concepts** including models, migrations, forms, views, templates, and URL routing.

---

# Application Preview

## Anime List Interface

![Anime List](crud_project/docs/anime-list.png)

The homepage displays stored anime entries and allows users to manage their collection.

Features shown in the interface:

- Anime title
- Main character
- Runtime
- Release year
- Genre classification
- Edit/Delete controls

---

## Edit Anime Interface

![Edit Anime](crud_project/docs/edit-anime.png)

The edit page allows updating any anime entry stored in the database.

Editable fields include:

- Title
- Main character
- Runtime
- Year of release
- Genre
- Rating
- Director
- Writer
- Cast
- Release date
- Gross revenue

---

## Django Admin Interface

### Admin List View
![Admin List](crud_project/docs/admin_pic_1.png)

### Admin Edit View
![Admin Edit](crud_project/docs/admin_pic_2.png)

### Admin Window View
![Admin List](crud_project/docs/anime-list.png)

### Admin Window Extended View
![Admin List](crud_project/docs/edit-anime.png)
---

# System Architecture

Browser  
│  
│ HTTP Request  
▼  
Django URL Router  
│  
▼  
View (views.py)  
│  
▼  
ModelForm (forms.py)  
│  
▼  
Model (models.py)  
│  
▼  
SQLite Database  

The response is then rendered through **Django Templates** and returned to the browser.

---

# Technology Stack

| Layer | Technology |
|------|------|
| Backend Framework | Django |
| Programming Language | Python |
| Database | SQLite |
| Frontend | Django Templates (HTML + CSS) |
| ORM | Django ORM |

---

# Project Structure

```
crud_project/

├── crud_project/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── anime_app/
│   ├── migrations/
│   ├── templates/
│   │   └── anime_app/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── edit_anime.html
│   │       └── delete_anime.html
│   │
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── docs/
│   ├── anime-list.png
│   ├── edit-anime.png
│   ├── admin_pic_1.png
│   └── admin_pic_2.png
│
└── manage.py
```

---

# Anime Data Model

The application stores anime records using the `Anime` model.

| Field | Type | Description |
|------|------|------|
| title | CharField | Anime title |
| main_character | CharField | Primary character |
| runtime | IntegerField | Runtime in minutes |
| year_of_release | IntegerField | Year the anime was released |
| genre | CharField (choices) | Genre classification |
| rating | CharField | Content rating |
| director | CharField | Director name |
| writer | CharField | Writer name |
| cast_star | CharField | Featured cast |
| release_date | DateField | Official release date |
| gross_revenue | BigIntegerField | Box office revenue |

---

# Installation

## Clone the repository

```
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd crud_project
```

---

## Create a virtual environment

```
python -m venv venv
```

Activate the environment.

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## Install dependencies

```
pip install django
```

---

## Apply database migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

## Run the development server

```
python manage.py runserver
```

Open the application:

http://127.0.0.1:8000

---

# Future Improvements

Potential enhancements for future development:

- Search functionality
- Genre filtering
- Pagination for large lists
- Anime poster images
- User authentication
- REST API using Django REST Framework
- Deployment to cloud hosting

---

# Learning Objectives

This project demonstrates key Django concepts:

- Model creation
- Database migrations
- Django ModelForms
- CRUD operations
- Template rendering
- URL routing
- ORM database interactions

---

# License

This project is intended for **educational and demonstration purposes**.
