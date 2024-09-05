# Niraj Bot Chat

Niraj Bot Chat is an AI-powered chat application that uses Google's Gemini AI model to provide intelligent responses to user queries. The application features a modern, responsive interface with dark mode support and the ability to manage multiple chat sessions.

## Features

- Real-time chat with AI-powered responses
- Dark mode toggle for comfortable viewing
- Multiple chat session support
- Responsive design using Tailwind CSS

## Technologies Used

- Backend:
  - Flask
  - Flask-SocketIO
  - Google Generative AI (Gemini)

- Frontend:
  - HTML5
  - JavaScript
  - Tailwind CSS
  - Socket.IO client

## Setup and Installation

1. Clone the repository:
   ```
   git clone https://github.com/your-username/niraj-bot-chat.git
   cd niraj-bot-chat
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your Google AI API key:
   - Obtain an API key from the Google AI Platform
   - Replace `'your-api-key'` in `app.py` with your actual API key

5. Run the application:
   ```
   python app.py
   ```

6. Open your web browser and navigate to `http://localhost:5001`

## Usage

- Start a new chat session by clicking the "Add New Chat" button
- Type your message in the input field and press "Send" or hit Enter
- Toggle between light and dark modes using the "Toggle Theme" button


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

