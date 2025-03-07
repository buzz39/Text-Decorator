# YayText - Unicode Text Styling System

YayText transforms ordinary text into stylized Unicode text with various fonts and decorative marks. This project provides both a Flask API and a Django web application to access Unicode text transformation functionality.

## 🌟 Features

- **Multiple Text Styles**: Bold, italic, script, monospace, and many more
- **Combining Diacritical Marks**: Underline, strikethrough, overline, etc.
- **API Access**: RESTful endpoints for programmatic use
- **Django Web Interface**: User-friendly UI for interactive styling

## 🚀 Live API

The API is deployed and accessible at:
```
https://text-helper-smoky.vercel.app
```

## 📋 API Documentation

### Get Available Styles

Returns all available text styling options and diacritical marks.

```
GET /api/styles
```

#### Response

```json
{
  "styles": ["bold", "italic", "bold_italic", "script", "bold_script", "fraktur", "double_struck", "sans_serif", "sans_bold", "sans_italic", "sans_bold_italic", "monospace"],
  "marks": {
    "underline": "COMBINING LOW LINE",
    "strikethrough": "COMBINING LONG STROKE OVERLAY",
    "double_underline": "COMBINING DOUBLE LOW LINE",
    "overline": "COMBINING OVERLINE",
    "double_overline": "COMBINING DOUBLE OVERLINE",
    "circle": "COMBINING ENCLOSING CIRCLE",
    "slash": "COMBINING LONG SOLIDUS OVERLAY"
  }
}
```

### Style Text

Transforms text using the specified style and optional diacritical marks.

```
POST /api/style
```

#### Request Body

```json
{
  "text": "Hello World",
  "style": "bold",
  "marks": ["underline", "overline"]
}
```

#### Response

```json
{
  "original": "Hello World",
  "styled": "𝐇̲̅𝐞̲̅𝐥̲̅𝐥̲̅𝐨̲̅ ̲̅𝐖̲̅𝐨̲̅𝐫̲̅𝐥̲̅𝐝̲̅",
  "style": "bold",
  "marks": ["underline", "overline"]
}
```

## 🔧 Local Development

### Prerequisites

- Python 3.7+
- pip

### Flask API Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd YayText
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask API:
   ```bash
   python api.py
   ```

4. The API will be available at `http://127.0.0.1:5000`

### Django Web App Setup

1. Install Django dependencies:
   ```bash
   pip install Django>=3.2.0
   ```

2. Run migrations:
   ```bash
   python manage.py migrate
   ```

3. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

4. The web interface will be available at `http://127.0.0.1:8000`

## 🧪 Usage Examples

### API Example (Python)

```python
import requests
import json

# Style text using the API
response = requests.post(
    "https://text-helper-smoky.vercel.app/api/style",
    headers={"Content-Type": "application/json"},
    data=json.dumps({
        "text": "Hello World",
        "style": "script",
        "marks": ["underline"]
    })
)

result = response.json()
print(result["styled"])  # Prints the styled text
```

### API Example (JavaScript)

```javascript
// Style text using the API
fetch('https://text-helper-smoky.vercel.app/api/style', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    text: 'Hello World',
    style: 'bold_italic',
    marks: ['strikethrough']
  }),
})
.then(response => response.json())
.then(data => {
  console.log(data.styled);  // Displays the styled text
})
.catch(error => {
  console.error('Error:', error);
});
```

## 🔒 Deployment

The project is deployed on Vercel. The configuration is defined in `vercel.json` which sets up the Python environment and routes for the Flask API.

## 📜 License

MIT License
