import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from easygoogletranslate import EasyGoogleTranslate
import detectlanguage

app = Flask(__name__)
CORS(app, origins=["*"])

load_dotenv()

# Load API keys from .env file
DETECT_LANGUAGE_API_KEY = os.environ.get("DETECT_LANGUAGE_API_KEY")
detectlanguage.configuration.api_key = DETECT_LANGUAGE_API_KEY

translator = EasyGoogleTranslate()

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

@app.route('/detect-and-translate', methods=['POST'])
def detect_and_translate():
    try:
        input_text = request.json.get('text')
        print(input_text)
        if not input_text:
            return jsonify({"error": "Missing 'text' in the request"}), 400

        detected_lang = detectlanguage.simple_detect(input_text)
        translated_text = translator.translate(input_text, target_language='en')

        return jsonify({
            "detected_language": detected_lang,
            "translated_text": translated_text
        }), 200

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/translate', methods=['POST'])
def translate():
    try:
        target_lang = request.json.get('target_language')
        english_text = request.json.get('text')

        if not target_lang or not english_text:
            return jsonify({"error": "Missing 'target_language' or 'text' in the request"}), 400

        translated_text = translator.translate(english_text, target_language=target_lang)

        return jsonify({
            "translated_text": translated_text
        }), 200

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/', methods=['GET'])
def root():
    return jsonify({
        "message": "Welcome to the Translation API",
        "endpoints": {
            "/health": "Check the health status of the API",
            "/detect-and-translate": "Detect language and translate to English",
            "/translate": "Translate from English to a target language"
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))