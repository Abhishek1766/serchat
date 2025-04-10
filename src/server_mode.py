from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/message', methods=['POST'])
def receive_message():
    data = request.get_json()
    message = data.get('message')
    print("Received message:", message)
    return jsonify({"status": "success", "message": message}), 200

def run_server():
    app.run(debug=True, port=5000)

class ChatServer:
    def run(self):
        print("Starting server...")
        run_server()  # Run the server in the main thread