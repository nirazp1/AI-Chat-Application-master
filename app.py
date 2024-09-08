from flask import Flask, render_template, request, session
from flask_socketio import SocketIO, emit
import google.generativeai as genai
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Configure Gemini
genai.configure(api_key='YOUR-SECRET-API-KEY')
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def index():
    print("Index route accessed") 
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print(f"Received message: {data}")  
    chat_id = data['chatId']
    message = data['message']
    
    # Process the message with Gemini model
    response = model.generate_content(message)
    response_text = response.text
    
    # Emit the response back to the client
    emit('message', {'chatId': chat_id, 'message': response_text})

if __name__ == '__main__':
    socketio.run(app, debug=True, port=5001)

