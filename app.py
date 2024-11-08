from flask import Flask, request, jsonify

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
