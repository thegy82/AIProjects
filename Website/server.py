from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import openai
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/generate-response', methods=['POST'])
def generate_response():
    prompt = request.json.get('prompt')
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"The following is a conversation with [Your Name]'s chatbot. The chatbot provides information about [Your Name].\n\nUser: {prompt}\nChatbot:",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return jsonify(response=response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(debug=True)
