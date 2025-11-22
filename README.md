# fastapi-mysql-demo
FastAPI + MySQL + SQLAlchemy (CRUD Demo)
This project is a simple, production-ready example of building a FastAPI backend application connected to a MySQL database using SQLAlchemy ORM.

It demonstrates:

FastAPI API development

SQLAlchemy model definitions

MySQL database integration

CRUD operations (Create, Read, Update, Delete)

Pydantic schema validation

Auto-generated Swagger UI

(Optional) Alembic migrations

Perfect for learning backend basics or creating YouTube tutorials.
````
📁 Folder Structure
fastapi-mysql-demo/
│
├── main.py                # FastAPI code
├── models.py              # SQLAlchemy table models
├── schemas.py             # Pydantic model
├── database.py            # MySQL connection 
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
````
🚀 Features

FastAPI backend with automatic docs (/docs)

MySQL database integration

SQLAlchemy ORM for defining models

Pydantic for request/response models

CRUD operations:
````
Create User

Get Users

Update User

Delete User
````
Clean modular project structure

Easy to extend into a full application

📦 Installation
```
1. Clone the project
git clone https://github.com/your-repo/fastapi-mysql-demo.git
cd fastapi-mysql-demo
````
🐍 Setup Python Environment
````
2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows
````
3. Install dependencies
````
pip install -r requirements.txt
````
If you don’t have a requirements.txt file yet, use:
```
fastapi
uvicorn
sqlalchemy
pydantic
````
🗄️ Setup MySQL Database
Option A — Use Local MySQL

Make sure MySQL is running and create a database:
````
CREATE DATABASE fastapi_demo;
````
Update your database.py:
````
DATABASE_URL = "mysql+mysqlconnector://root:password@localhost:3306/fastapi_demo"
````
Option B — Run MySQL in Docker
````
docker run --name mysql \
  -e MYSQL_ROOT_PASSWORD=password \
  -e MYSQL_DATABASE=fastapi_demo \
  -p 3306:3306 \
  -d mysql:8
````
🧠 Understanding SQLAlchemy Files

database.py
Creates MySQL engine + session factory

models.py
Defines database tables using ORM classes

schemas.py
Defines request/response validation models

main.py
Contains:

API routes

CRUD operations

Database session handling

Automatic table creation

▶️ Running the FastAPI Server

Start the backend:

uvicorn main:app --reload


FastAPI will be available at:
````
📍 http://127.0.0.1:8000

📄 Swagger Docs: http://127.0.0.1:8000/docs
````
📌 API Endpoints
Method	Endpoint	Description
POST	/users	Create new user
GET	/users	List all users
PUT	/users/{id}	Update user
DELETE	/users/{id}	Delete user
