# LangAPI

LangAPI is a Flask-based RESTful API that provides language detection and translation services. It leverages the power of Google Translate and DetectLanguage to offer robust language processing capabilities.

## Features

- Language detection for input text
- Translation of text from any language to English
- Translation of English text to any supported language
- Health check endpoint

## Prerequisites

- Python 3.7+
- pip (Python package manager)

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/K-Jadeja/langAPI.git
   cd langapi
   ```

2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   Create a `.env` file in the root directory and add your DetectLanguage API key:
   ```
   DETECT_LANGUAGE_API_KEY=your_api_key_here
   ```

## Usage

To run the server locally:

```
python main.py
```

The API will be available at `http://localhost:5000`.

## API Endpoints

### Health Check

- **GET** `/health`
  - Returns the health status of the API

### Detect and Translate

- **POST** `/detect-and-translate`
  - Detects the language of the input text and translates it to English
  - Request body: `{ "text": "Your text here" }`

### Translate

- **POST** `/translate`
  - Translates English text to the specified target language
  - Request body: `{ "target_language": "fr", "text": "Your English text here" }`

## Testing

To run the test script:
`python test.py`

## Deployment

This project is configured for deployment on Vercel. The `vercel.json` file in the root directory contains the necessary configuration.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
