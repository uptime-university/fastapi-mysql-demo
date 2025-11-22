
# fastapi-mysql-demo

A clean, minimal, and production-minded example of a FastAPI backend using MySQL with SQLAlchemy. This repository demonstrates how to structure a small API project, validate requests with Pydantic, and perform basic CRUD operations against a MySQL database.

Highlights
- FastAPI backend with auto-generated OpenAPI / Swagger UI
- SQLAlchemy ORM models and session management
- Pydantic request/response schemas
- CRUD endpoints for a simple "User" resource
- Optional Alembic migrations (when added)
- Small, modular code layout ideal for learning or as a starting template

Table of Contents
- About
- Features
- Project structure
- Quick start
  - Requirements
  - Install
  - Environment
  - Database setup (local / Docker)
  - Run
- API reference (endpoints + examples)
- Development notes
- Contributing
- License

About
This demo aims to be easy to read and extend. It's intended for developers who want a compact example of integrating FastAPI with a MySQL database via SQLAlchemy.

Features
- FastAPI routes and automatic docs at /docs
- SQLAlchemy ORM for DB models and sessions
- Pydantic schemas for request/response validation
- CRUD operations: create, read, update, delete users
- Clear separation of responsibilities (main, models, schemas, database)
- Ready to extend: add authentication, migrations, tests, etc.

Project structure
fastapi-mysql-demo/
- main.py                # FastAPI application, routes, CRUD handlers
- models.py              # SQLAlchemy ORM models
- schemas.py             # Pydantic models (request/response)
- database.py            # DB engine & session factory
- requirements.txt       # Python dependencies
- README.md              # Project documentation

Quick start

Requirements
- Python 3.9+ (3.11 recommended)
- MySQL server (local, remote, or docker)
- pip

Install
1. Clone
```bash
git clone https://github.com/uptime-university/fastapi-mysql-demo.git
cd fastapi-mysql-demo
```

2. Create & activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows (PowerShell)
```

3. Install dependencies
```bash
pip install -r requirements.txt
```
If your environment does not include a requirements file, at minimum install:
```bash
pip install fastapi uvicorn sqlalchemy mysql-connector-python pydantic
```
(You can replace mysql-connector-python with mysqlclient if preferred — adjust DATABASE_URL accordingly.)

Environment (DATABASE_URL)
Configure the connection string used by database.py. Example:
- Using mysql-connector: mysql+mysqlconnector://root:password@localhost:3306/fastapi_demo
- Using mysqlclient (MySQLdb): mysql+mysqldb://root:password@localhost:3306/fastapi_demo

Set it in a .env file or export as an environment variable and ensure database.py reads it (or update the constant directly for testing).

Database setup

Option A — Local MySQL
1. Ensure MySQL server running.
2. Create a database:
```sql
CREATE DATABASE fastapi_demo CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```
3. Update DATABASE_URL in database.py or via env var.

Option B — MySQL with Docker
If you prefer a disposable local DB, run:
```bash
docker run --name fastapi-mysql-demo-mysql \
  -e MYSQL_ROOT_PASSWORD=password \
  -e MYSQL_DATABASE=fastapi_demo \
  -p 3306:3306 \
  -d mysql:8
```
Then use:
mysql+mysqlconnector://root:password@127.0.0.1:3306/fastapi_demo

Note about migrations
This project optionally supports Alembic for migrations. Alembic is not included by default here; you can add alembic and an alembic.ini if you want to manage schema changes safely in production.

Run the server
Start the FastAPI app with uvicorn:
```bash
uvicorn main:app --reload
```
By default the server will be available at:
- http://127.0.0.1:8000
- Swagger UI (interactive docs): http://127.0.0.1:8000/docs

API reference (basic endpoints)
The project provides a small set of endpoints for a "User" entity:

- POST /users — Create a user
- GET /users — List all users
- PUT /users/{id} — Update a user by id
- DELETE /users/{id} — Delete a user by id

Example usage (curl)

Create user
```bash
curl -X POST "http://127.0.0.1:8000/users" \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice","email":"alice@example.com"}'
```

List users
```bash
curl http://127.0.0.1:8000/users
```

Update user
```bash
curl -X PUT "http://127.0.0.1:8000/users/1" \
  -H "Content-Type: application/json" \
  -d '{"name":"Alice B.","email":"alice.b@example.com"}'
```

Delete user
```bash
curl -X DELETE "http://127.0.0.1:8000/users/1"
```

Development notes
- database.py: creates the SQLAlchemy engine and SessionLocal. Ensure sessions are closed after each request (dependency injection pattern is recommended).
- models.py: defines the User model (fields such as id, name, email, timestamps).
- schemas.py: Pydantic models for request and response validation.
- main.py: wires routes, CRUD operations, and the DB session dependency. Consider adding pagination, filters, and better error handling for production-ready APIs.
- Logging & configuration: For production, add structured logging and a settings module (pydantic BaseSettings or similar).

Testing
- Add unit tests and integration tests (pytest recommended).
- For DB tests, use a separate test database or an in-memory alternative where applicable, and consider fixtures to set up/tear down test data.

Contributing
- Contributions and improvements are welcome.
- Please open issues or pull requests for bug fixes, feature requests, or documentation improvements.
- Follow standard GitHub best practices: small focused PRs, descriptive commit messages, and tests when applicable.

License
This repository is provided as-is for educational purposes. Add a LICENSE file to declare the desired license.

Acknowledgements
- FastAPI (https://fastapi.tiangolo.com)
- SQLAlchemy (https://www.sqlalchemy.org)

If you'd like, I can:
- polish this README further with badges and screenshots,
- add a docker-compose.yml example to run the app + MySQL together,
- or produce an Alembic example for migrations.
````
