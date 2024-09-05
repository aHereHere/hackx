from flask import Flask, request, jsonify
from googletrans import Translator
import requests

app = Flask(__name__)
translator = Translator()

@app.route('/translate', methods=['POST'])
def translate_and_forward():
    data = request.json
    if 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    original_text = data['text']
    
    # Translate to English
    translation = translator.translate(original_text,src='hi', dest='en')
    translated_text = translation.text

    # Send to another service
    

    return jsonify({
        'original_text': original_text,
        'translated_text': translated_text,
        'forwarded': True
    })

if __name__ == '__main__':
    # Run the Flask app on a specific host and port
    app.run(host='0.0.0.0', port=5000, debug=True)

# To run this server in Cursor IDE:
# 1. Save this file (e.g., as 'app.py')
# 2. Open a terminal in Cursor IDE
# 3. Navigate to the directory containing this file
# 4. Run the following command:
#    python app.py
#
# The server will start and be accessible at http://localhost:5000
# You can then use tools like curl or Postman to send POST requests to http://localhost:5000/translate

