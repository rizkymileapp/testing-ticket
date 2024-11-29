# Ticket Hint

Ticket Hint is a Mini AI Project built with Flask that accepts input questions and processes them to provide the desired output.

## 📋 Features
- Accepts question inputs (tickets) via an API endpoint.
- Returns suggestions for the inputted ticket in a JSON response.

## 🛠️ Technologies Used
- Python 3.10
- Flask (Python Web Framework)

## 📦 Installation

### 1. Clone Repository
Clone this repository to your computer:
```
git clone https://github.com/rizkymileapp/testing-ticket.git
cd testing-ticket
```

### 2. Create and Activate a Virtual Environment
Create a virtual environment to isolate the project:
```
python -m venv venv
venv\Scripts\activate
```

### 3. Instal Dependencies
Install Flask and other required dependencies:
```
pip install -r requirements.txt
```

### 4. Run the Application
Run the Flask application with the following command:
```
python app.py
```
The application will be available at `http://127.0.0.1:5000/`.

### 5. Using cURL
You can test the API using cURL or Postman.
```
curl -X POST http://127.0.0.1:5000/ticket-response \
-H "Content-Type: application/json" \
-d "{\"question\": \"Saya tidak bisa login ke akun saya\"}"
```



