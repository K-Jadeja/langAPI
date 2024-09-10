import os
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from easygoogletranslate import EasyGoogleTranslate
import detectlanguage

app = Flask(__name__)
CORS(app, origins=["*"])

load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Loading API keys from .env file")
# Load API keys from .env file
DETECT_LANGUAGE_API_KEY = os.environ.get("DETECT_LANGUAGE_API_KEY")
detectlanguage.configuration.api_key = DETECT_LANGUAGE_API_KEY

logger.info("Initializing EasyGoogleTranslate")
translator = EasyGoogleTranslate()

@app.route('/health', methods=['GET'])
def health():
    logger.info("Health check requested")
    return jsonify({"status": "healthy"}), 200

@app.route('/detect-and-translate', methods=['POST'])
def detect_and_translate():
    logger.info("Detect and translate request received")
    try:
        input_text = request.json.get('text')
        logger.info(f"Input text: {input_text}")
        if not input_text:
            logger.warning("Missing 'text' in the request")
            return jsonify({"error": "Missing 'text' in the request"}), 400

        logger.info("Detecting language")
        detected_lang = detectlanguage.simple_detect(input_text)
        logger.info(f"Detected language: {detected_lang}")

        logger.info("Translating text to English")
        translated_text = translator.translate(input_text, target_language='en')
        logger.info(f"Translated text: {translated_text}")

        return jsonify({
            "detected_language": detected_lang,
            "translated_text": translated_text
        }), 200

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/translate', methods=['POST'])
def translate():
    logger.info("Translation request received")
    try:
        target_lang = request.json.get('target_language')
        english_text = request.json.get('text')
        logger.info(f"Target language: {target_lang}")
        logger.info(f"English text: {english_text}")

        if not target_lang or not english_text:
            logger.warning("Missing 'target_language' or 'text' in the request")
            return jsonify({"error": "Missing 'target_language' or 'text' in the request"}), 400

        logger.info("Translating text")
        translated_text = translator.translate(english_text, target_language=target_lang)
        logger.info(f"Translated text: {translated_text}")

        return jsonify({
            "translated_text": translated_text
        }), 200

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.route('/', methods=['GET'])
def root():
    logger.info("Root endpoint accessed")
    return jsonify({
        "message": "Welcome to the Translation API",
        "endpoints": {
            "/health": "Check the health status of the API",
            "/detect-and-translate": "Detect language and translate to English",
            "/translate": "Translate from English to a target language"
        }
    }), 200

if __name__ == '__main__':
    port = os.getenv("PORT", default=5000)
    logger.info(f"Starting the application on port {port}")
    app.run(debug=True, port=port)