PythonRamp - Transaction Management API

Showcase: Fully functioning backend API with asynchronous database handling, validation, and automated tests — perfect for demonstrating your Python and FastAPI skills to employers.

A simple FastAPI backend project that allows creating, approving, and rejecting transactions. This project demonstrates Python, FastAPI, SQLAlchemy (async), and testing with pytest.

▶️ Key Highlights

Complete CRUD backend for transaction management

Async database handling using SQLAlchemy

Input validation for invalid or duplicate actions

Fully tested with pytest (all tests passing ✅)

Clear and professional project structure for employers

🛠 Technologies Used

Python 3.13

FastAPI – Web framework for building APIs

SQLAlchemy (Async) – ORM for database management

SQLite – Local database for development

pytest – Automated testing framework

Uvicorn – ASGI server for running FastAPI

📂 Project Structure
PythonRamp/
├─ main.py              # FastAPI application with endpoints
├─ models.py            # Database models (Transaction)
├─ database.py          # Async database setup
├─ test_database.py     # Test DB setup
├─ test_transactions.py # Unit tests for API endpoints
├─ .venv/               # Virtual environment
└─ README.md            # Project documentation

▶️ Run the App Locally

Clone the repository:

git clone https://github.com/trinityray02/PythonRamp.git
cd PythonRamp


Activate the virtual environment:

source .venv/bin/activate


Install dependencies (if not installed):

pip install -r requirements.txt


Run the FastAPI server:

uvicorn main:app --reload


Access the API documentation:
Open http://127.0.0.1:8000/docs
 in your browser.

✅ Run Tests

Run all automated tests using pytest:

pytest -q


All tests should pass:

.... [100%]
4 passed in X.XXs

🔗 API Endpoints
Endpoint	Method	Description
/transactions	POST	Create a new transaction
/transactions/{id}/approve	POST	Approve a pending transaction
/transactions/{id}/reject	POST	Reject a pending transaction
/	GET	Health check ({"status":"ok"})

Request Example:

POST /transactions
{
  "amount": 100
}


Response Example:

{
  "id": 1,
  "amount": 100.0,
  "status": "pending"
}

📌 Notes for Employers

Demonstrates full backend functionality, including async database, validation, and testing.

Can be extended with frontend integration or deployed online.

All tests pass, ensuring reliability and stability.

👋 About Me / Contact

Hi! I’m Trinity Ray, a full-stack developer passionate about building clean, efficient, and tested web applications.

GitHub: github.com/trinityray02

Email: trinityelisha02.com

LinkedIn: linkedin.com/in/trinityray

I’m actively seeking internships and full-time opportunities where I can contribute my skills and continue learning.
