# fastapi-task-manager
# 📝 FastAPI Task Manager API

A simple and secure Task Manager built with **FastAPI**, **JWT Authentication**, and **SQLAlchemy**. Users can register, log in, and manage their own tasks through a RESTful API.

---

## 🚀 Features

- ✅ User registration & login (with JWT tokens)
- 🔐 Password hashing using `passlib`
- ✅ Create, Read, Update, Delete (CRUD) tasks
- 👤 Task access restricted to the task owner
- 🧩 SQLite + SQLAlchemy ORM
- 📜 Auto-generated Swagger UI docs
- 🧪 Clean modular structure for easy scaling

---

## 🧱 Project Structure
fastapi-task-manager/
├── app/
│ ├── main.py # Entry point
│ ├── database.py # DB setup
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ ├── auth.py # Auth logic
│ └── routers/
│ ├── users.py # /auth routes
│ └── tasks.py # /tasks routes
├── requirements.txt
└── README.md


---

## ⚙️ Setup Instructions

### 1. Clone the repo & install dependencies

```bash
git clone https://github.com/yourusername/fastapi-task-manager.git
cd fastapi-task-manager

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate   # or venv\\Scripts\\activate on Windows

# Install required packages
pip install -r requirements.txt

2. Run the app
```bash
uvicorn app.main:app --reload
```
🔐 API Auth Flow
Register via POST /auth/register

Login via POST /auth/login → receive access_token

Use Bearer <access_token> for all /tasks endpoints


✅ Example Endpoints
POST /auth/register

POST /auth/login

GET /tasks/

POST /tasks/

PUT /tasks/{id}

DELETE /tasks/{id}



📦 Dependencies
fastapi

uvicorn

sqlalchemy

passlib[bcrypt]

python-jose

pydantic