from flask import Flask, request, jsonify
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import os

app = Flask(__name__)

load_dotenv()

freshdesk_api_key = os.getenv("FRESHDESK_API_KEY")
freshdesk_domain = os.getenv("FRESHDESK_DOMAIN")

# Endpoint Root
@app.route('/', methods=['GET'])
def home():
    return "Ticket Hint"

# Endpoint API
@app.route('/ticket-response', methods=['POST'])
def ticket_response():
    # Ambil data dari permintaan
    data = request.get_json()
    question = data.get('question', '')

    # Validasi input
    if not question:
        return jsonify({
            'status': False,
            'message': 'Question is required'
        }), 400

    # Respons statis
    response_text = "Noted, this ticket is well received. In the future, this text will be replaced by an AI agent to assist you in resolving the ticket."
    
    # Kirim respons JSON
    return jsonify({
        'status': True, 
        'ticket': question,
        'message': response_text
    })

# Endpoint untuk menerima data dari webhook
@app.route('/ticket-webhook', methods=['POST'])
def handle_webhook():
    try:
        # Ambil data dari permintaan
        data = request.get_json()
        freshdesk_data = data.get('freshdesk_webhook', {})

        # Validasi input yang diperlukan
        ticket_id = freshdesk_data.get('ticket_id')
        ticket_subject = freshdesk_data.get('ticket_subject')
        ticket_description = freshdesk_data.get('ticket_description')

        if not ticket_id or not ticket_subject or not ticket_description:
            return jsonify({
                'status': False,
                'message': 'ticket_id, ticket_subject, and ticket_description are required'
            }), 400

        # Proses untuk hit endpoint Freshdesk
        freshdesk_url = f"https://{freshdesk_domain}/api/v2/tickets/{ticket_id}/notes"

        note_data = {
            "body": "Noted, this ticket is well received. In the future, this text will be replaced by an AI agent to assist you in resolving the ticket.",
            "private": True,
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(
            freshdesk_url,
            json=note_data,
            headers=headers,
            auth=(freshdesk_api_key, "X")
        )

        # Ekstrak teks dari HTML di ticket_description
        soup = BeautifulSoup(ticket_description, "html.parser")
        extracted_text = soup.get_text(strip=True)

        # Periksa respons dari Freshdesk API
        if response.status_code == 201:
            return jsonify({
                'status': True,
                'message': 'Note successfully created on Freshdesk',
                'data': response.json(),
                'ticket': extracted_text
            }), 201
        else:
            return jsonify({
                'status': False,
                'message': 'Failed to create note on Freshdesk',
                'error': response.json()
            }), response.status_code

    except Exception as e:
        return jsonify({
            'status': False,
            'message': 'An error occurred',
            'error': str(e)
        }), 500

if __name__ == '__main__':
    app.run(debug=True)