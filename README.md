# Text Decorator - Unicode Text Styling System

Text Decorator transforms ordinary text into stylized Unicode text with various fonts and decorative marks. This project provides both a Flask API and a Django web application to access Unicode text transformation functionality.

## 🌟 Features

- **30+ Text Styles**: Mathematical alphanumeric symbols, fullwidth, bubble text, superscript, subscript, and many more
- **80+ Combining Diacritical Marks**: Underline, strikethrough, overline, tilde, macron, cedilla, and many more
- **API Access**: RESTful endpoints for programmatic use
- **Django Web Interface**: User-friendly UI for interactive styling

## 🎨 Available Text Styles

### Mathematical Alphanumeric Symbols
- **bold** - 𝐁𝐨𝐥𝐝 𝐭𝐞𝐱𝐭
- **italic** - 𝐼𝑡𝑎𝑙𝑖𝑐 𝑡𝑒𝑥𝑡
- **bold_italic** - 𝑩𝒐𝒍𝒅 𝒊𝒕𝒂𝒍𝒊𝒄 𝒕𝒆𝒙𝒕
- **script** - 𝒮𝒸𝓇𝒾𝓅𝓉 𝓉𝑒𝓍𝓉
- **bold_script** - 𝓑𝓸𝓵𝓭 𝓼𝓬𝓻𝓲𝓹𝓽 𝓽𝓮𝔁𝓽
- **fraktur** - 𝔉𝔯𝔞𝔨𝔱𝔲𝔯 𝔱𝔢𝔵𝔱
- **bold_fraktur** - 𝕭𝖔𝖑𝖉 𝖋𝖗𝖆𝖐𝖙𝖚𝖗 𝖙𝖊𝖝𝖙
- **double_struck** - 𝔻𝕠𝕦𝕓𝕝𝕖 𝕤𝕥𝕣𝕦𝕔𝕜 𝕥𝕖𝕩𝕥
- **sans_serif** - 𝖲𝖺𝗇𝗌 𝗌𝖾𝗋𝗂𝖿 𝗍𝖾𝗑𝗍
- **sans_bold** - 𝗦𝗮𝗻𝘀 𝗯𝗼𝗹𝗱 𝘁𝗲𝘅𝘁
- **sans_italic** - 𝘚𝘢𝘯𝘴 𝘪𝘵𝘢𝘭𝘪𝘤 𝘵𝘦𝘹𝘵
- **sans_bold_italic** - 𝙎𝙖𝙣𝙨 𝙗𝙤𝙡𝙙 𝙞𝙩𝙖𝙡𝙞𝙘 𝙩𝙚𝙭𝙩
- **monospace** - 𝙼𝚘𝚗𝚘𝚜𝚙𝚊𝚌𝚎 𝚝𝚎𝚡𝚝

### Special Unicode Styles
- **fullwidth** - Ｆｕｌｌｗｉｄｔｈ　ｔｅｘｔ
- **small_caps** - ꜱᴍᴀʟʟ ᴄᴀᴘꜱ ᴛᴇxᴛ
- **superscript** - ˢᵘᵖᵉʳˢᶜʳⁱᵖᵗ ᵗᵉˣᵗ
- **subscript** - ₛᵤᵦₛcᵣᵢₚₜ ₜₑₓₜ
- **bubble_text** - Ⓑⓤⓑⓑⓛⓔ ⓣⓔⓧⓣ
- **black_bubble_text** - 🅑🅛🅐🅒🅚 🅑🅤🅑🅑🅛🅔 🅣🅔🅧🅣
- **square_text** - 🅂🅀🅄🄰🅁🄴 🅃🄴🅇🅃
- **upside_down** - ʇxǝʇ uʍop ǝpᴉsdn
- **parenthesized** - ⒫⒜⒭⒠⒩⒯⒣⒠⒮⒤⒵⒠Ⓓ ⒯⒠⒳⒯
- **regional_indicator** - 🇷🇪🇬🇮🇴🇳🇦🇱 🇮🇳🇩🇮🇨🇦🇹🇴🇷
- **weird_text** - Ⱳɇɨɍđ ŧɇẋŧ
- **cherokee_like** - Ꮯꮋꭼꮢꮎꮶꭼꭼ ꮮꭵꮶꭼ ꮏꭼꮝꮏ

### Math Digit Styles
- **math_bold_digits** - 𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗
- **math_double_struck_digits** - 𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡
- **math_sans_serif_digits** - 𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫
- **math_sans_bold_digits** - 𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵
- **math_monospace_digits** - 𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿

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
  "styles": [
    "bold", "italic", "bold_italic", "script", "bold_script", "fraktur",
    "double_struck", "sans_serif", "sans_bold", "sans_italic", "sans_bold_italic",
    "monospace", "bold_fraktur", "fullwidth", "small_caps", "superscript",
    "subscript", "bubble_text", "black_bubble_text", "square_text", "upside_down",
    "parenthesized", "regional_indicator", "weird_text", "cherokee_like",
    "math_bold_digits", "math_double_struck_digits", "math_sans_serif_digits",
    "math_sans_bold_digits", "math_monospace_digits"
  ],
  "marks": {
    "underline": "COMBINING LOW LINE",
    "strikethrough": "COMBINING LONG STROKE OVERLAY",
    "double_underline": "COMBINING DOUBLE LOW LINE",
    "overline": "COMBINING OVERLINE",
    "double_overline": "COMBINING DOUBLE OVERLINE",
    "circle": "COMBINING ENCLOSING CIRCLE",
    "slash": "COMBINING LONG SOLIDUS OVERLAY",
    "tilde": "COMBINING TILDE",
    "macron": "COMBINING MACRON",
    "dot_above": "COMBINING DOT ABOVE",
    "ring_above": "COMBINING RING ABOVE",
    "cedilla": "COMBINING CEDILLA",
    "... and 75+ more combining marks"
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
  "text": "Text Decorator",
  "style": "bold",
  "marks": ["underline", "overline"]
}
```

#### Response

```json
{
  "original": "Text Decorator",
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
   cd text-decorator
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
        "text": "Text Decorator",
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

## 🆕 What's New

This Text Decorator API has been significantly expanded with:

- **18 new text styles** including fullwidth, bubble text, superscript, subscript, upside down, and more
- **75+ additional combining marks** for extensive text decoration options
- **Mathematical alphanumeric symbols** from Unicode Mathematical Alphanumeric Symbols block
- **Creative Unicode transformations** inspired by YayText.com and YayText.vn websites
- **Regional indicator symbols** for flag-style text
- **Cherokee-like and weird text** styles for unique effects
- **🇻🇳 Vietnamese language support** with proper handling of diacritics and tone marks

Total: **30 text styles**, **82 combining marks**, and **Vietnamese language support** available!

## 🇻🇳 Vietnamese Language Support

The API now includes comprehensive Vietnamese language support with:

- **178 Vietnamese characters** including all tone mark variations
- **Proper diacritics handling** for ă, â, ê, ô, ơ, ư, đ
- **Tone mark preservation** for all 5 Vietnamese tones (grave, acute, hook above, tilde, dot below)
- **Smart text detection** to automatically identify Vietnamese text
- **Unicode normalization** to handle composed and decomposed characters correctly

### Vietnamese API Endpoints

#### Get Language Information
```http
GET /api/language
```

#### Style Vietnamese Text
```http
POST /api/language/vietnamese
```

**Request Body:**
```json
{
  "text": "Xin chào Việt Nam",
  "style": "bold",
  "marks": ["tilde"],
  "auto_detect": true
}
```

**Response:**
```json
{
  "original": "Xin chào Việt Nam",
  "styled": "𝐗𝐢𝐧 𝐜𝐡𝐚̀𝐨 𝐕𝐢𝐞̣̂𝐭 𝐍𝐚𝐦",
  "style": "bold",
  "marks": ["tilde"],
  "language": "vietnamese",
  "is_vietnamese": true,
  "characters_count": 14
}
```

#### Detect Vietnamese Text
```http
POST /api/language/detect
```

**Request Body:**
```json
{
  "text": "Tiếng Việt rất đẹp"
}
```

**Response:**
```json
{
  "text": "Tiếng Việt rất đẹp",
  "is_vietnamese": true,
  "detected_language": "vietnamese",
  "vietnamese_characters": ["T", "i", "ế", "n", "g", "V", "i", "ệ", "t", "r", "ấ", "t", "đ", "ẹ", "p"],
  "vietnamese_char_count": 15,
  "confidence": 0.83
}
```

## 📜 License

MIT License
