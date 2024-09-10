# LangAPI Documentation

Base URL: `https://one-lang-api.vercel.app`

## Endpoints

### 1. Health Check

**GET** `/health`

Check the health status of the API.

#### Request

```javascript
fetch('https://one-lang-api.vercel.app/health')
  .then(response => response.json())
  .then(data => console.log(data));
```

#### Response

```json
{
  "status": "healthy"
}
```

### 2. Detect and Translate

**POST** `/detect-and-translate`

Detects the language of the input text and translates it to English.

#### Request

```javascript
const response = await fetch('https://one-lang-api.vercel.app/detect-and-translate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: "Bonjour le monde"
  }),
});
const data = await response.json();
```

#### Response

```json
{
  "detected_language": "fr",
  "translated_text": "Hello world"
}
```

### 3. Translate

**POST** `/translate`

Translates English text to the specified target language.

#### Request

```javascript
const response = await fetch('https://one-lang-api.vercel.app/translate', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    target_language: "fr",
    text: "Hello world"
  }),
});
const data = await response.json();
```

#### Response

```json
{
  "translated_text": "Bonjour le monde"
}
```

## Error Handling

All endpoints may return error responses in the following format:

```json
{
  "error": "Error message description"
}
```

Common HTTP status codes:
- 200: Successful request
- 400: Bad request (e.g., missing parameters)
- 500: Internal server error

## Usage with Next.js

To use this API in a Next.js application, you can create a utility function for API calls:

```javascript
// utils/api.js

const API_BASE_URL = 'https://one-lang-api.vercel.app';

export async function detectAndTranslate(text) {
  const response = await fetch(`${API_BASE_URL}/detect-and-translate`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text }),
  });
  return response.json();
}

export async function translate(text, targetLanguage) {
  const response = await fetch(`${API_BASE_URL}/translate`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ text, target_language: targetLanguage }),
  });
  return response.json();
}
```

Then, you can use these functions in your Next.js components or pages:

```javascript
import { detectAndTranslate, translate } from '../utils/api';

export default function TranslationComponent() {
  const [result, setResult] = useState(null);

  const handleDetectAndTranslate = async () => {
    const data = await detectAndTranslate('Bonjour le monde');
    setResult(data);
  };

  const handleTranslate = async () => {
    const data = await translate('Hello world', 'fr');
    setResult(data);
  };

  return (
    <div>
      <button onClick={handleDetectAndTranslate}>Detect and Translate</button>
      <button onClick={handleTranslate}>Translate to French</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </div>
  );
}
```

Remember to handle errors and loading states in your Next.js application for a better user experience.
