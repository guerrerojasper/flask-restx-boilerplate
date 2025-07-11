# 🧪 Flask RESTx Boilerplate

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-%232c3e50?logo=flask&logoColor=white)
![Flask-RESTx](https://img.shields.io/badge/Flask--RESTx-009688?logo=swagger&logoColor=white)
![Flask-Migrate](https://img.shields.io/badge/Flask--Migrate-003545?logo=flask&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?logo=mongodb&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-CA2C39?logo=sqlalchemy&logoColor=white)

A boilerplate Flask project that integrates **Flask-RESTx** for powerful API documentation, **SQLAlchemy** and **MongoEngine** for flexible database support, **Flask-Migrate** for schema versioning, and **Pytest** for comprehensive testing.

---

## 🚀 Tech Stack

| Tool / Library       | Purpose                                   |
|----------------------|--------------------------------------------|
|  Python 3.9+        | Core language                             |
|  Flask             | Web framework                             |
|  Flask-RESTx        | API framework with Swagger UI             |
|  SQLAlchemy        | ORM for relational databases              |
|  MongoEngine        | ODM for MongoDB                           |
|  Flask-Migrate      | SQLAlchemy schema migrations              |
|  Pytest             | Unit testing framework                    |

---

## 📦 Features

- Built-in support for RESTful APIs via Flask-RESTx
- Auto-generated Swagger documentation
- Dual DB support: SQL (via SQLAlchemy) and NoSQL (via MongoDB)
- Migration-ready using Flask-Migrate
- Pytest-based testing suite with fixtures
- Structured application layout

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/guerrerojasper/flask-restx-boilerplate.git
cd flask-restx-boilerplate

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Running Tests
```bash
# Run all unit tests
pytest
```
You can also add flags for detailed output:
```bash
pytest -v --tb=short
```

---

## 🔌 Database Setup
**SQLAlchemy (PostgreSQL/MySQL/etc)**
Make sure to configure your SQL DB URI in .env:
```bash
SQLALCHEMY_DATABASE_URI=postgresql://user:password@localhost/db_name
```
Then run migrations:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```
**MongoDB**
If you're using MongoDB instead, configure it via:
```bash
MONGODB_URI=mongodb://localhost:27017/your_db
```

---

## 📚 API Documentation
Once the app is running, visit:
```bash
http://localhost:5000/swagger
```

---

## 🗂️ Project Structure
```bash
flask-restx-boilerplate/
├── app/
│   ├── document/           # MongoEngine models
│   ├── models/             # SQLAlchemy and MongoEngine models
│   ├── schemas/            # Input/output schemas
│   ├── routes/             # Business logic (controller and model)
│   ├── config.py           # Configuration settings
│   ├── register.py         # Routes confiurations
│   └── __init__.py         # API Initialization
├── tests/                  # Pytest unit tests
├── migrations/             # Flask-Migrate data
└── run.py                  # App entry point
```
