from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/message', methods=['POST'])
def receive_message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Invalid input"}), 400  # Return a 400 error if input is invalid
    message = data['message']
    print("Received message:", message)
    return jsonify({"status": "success", "message": message}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000)