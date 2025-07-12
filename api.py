from flask import Flask, request, jsonify
from flask_cors import CORS
import unicodedata
from app import (
    style_text, add_diacritics, STYLE_CONFIG, COMBINING_MARKS,
    is_vietnamese_text, style_vietnamese_text, get_vietnamese_language_info,
    VIETNAMESE_CHARACTERS, VIETNAMESE_TONE_MARKS
)

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/styles', methods=['GET'])
def get_styles():
    """Return all available text styles"""
    return jsonify({
        "styles": list(STYLE_CONFIG.keys()),
        "marks": {k: unicodedata.name(v) for k, v in COMBINING_MARKS.items()}
    })

@app.route('/api/style', methods=['POST'])
def style():
    """Style the provided text"""
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Missing text parameter"}), 400
    
    text = data['text']
    style_name = data.get('style', 'bold')
    marks = data.get('marks', [])
    
    # Check if style exists
    if style_name not in STYLE_CONFIG:
        return jsonify({"error": f"Style '{style_name}' not found"}), 400
    
    # Apply styling
    styled_text = style_text(text, style_name)
    
    # Apply marks if specified
    if marks:
        mark_chars = []
        for mark_name in marks:
            if mark_name in COMBINING_MARKS:
                mark_chars.append(COMBINING_MARKS[mark_name])
        
        if mark_chars:
            styled_text = add_diacritics(styled_text, mark_chars)
    
    return jsonify({
        "original": text,
        "styled": styled_text,
        "style": style_name,
        "marks": marks
    })

@app.route('/api/language', methods=['GET'])
def get_language_info():
    """Get information about supported languages"""
    return jsonify({
        "supported_languages": ["vietnamese"],
        "vietnamese": get_vietnamese_language_info()
    })

@app.route('/api/language/vietnamese', methods=['POST'])
def style_vietnamese():
    """Style Vietnamese text with proper handling of diacritics and tone marks"""
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Missing text parameter"}), 400

    text = data['text']
    style_name = data.get('style', 'bold')
    marks = data.get('marks', [])
    auto_detect = data.get('auto_detect', True)

    # Validate that it's Vietnamese text if auto_detect is enabled
    if auto_detect and not is_vietnamese_text(text):
        return jsonify({
            "warning": "Text does not appear to contain Vietnamese characters",
            "is_vietnamese": False,
            "original": text,
            "styled": text,
            "style": style_name,
            "marks": marks
        })

    # Check if style exists
    if style_name not in STYLE_CONFIG:
        return jsonify({"error": f"Style '{style_name}' not found"}), 400

    # Apply Vietnamese-aware styling
    styled_text = style_vietnamese_text(text, style_name)

    # Apply marks if specified
    if marks:
        mark_chars = []
        for mark_name in marks:
            if mark_name in COMBINING_MARKS:
                mark_chars.append(COMBINING_MARKS[mark_name])
            elif mark_name in VIETNAMESE_TONE_MARKS:
                mark_chars.append(VIETNAMESE_TONE_MARKS[mark_name])

        if mark_chars:
            styled_text = add_diacritics(styled_text, mark_chars)

    return jsonify({
        "original": text,
        "styled": styled_text,
        "style": style_name,
        "marks": marks,
        "language": "vietnamese",
        "is_vietnamese": is_vietnamese_text(text),
        "characters_count": len([c for c in text if c in VIETNAMESE_CHARACTERS])
    })

@app.route('/api/language/detect', methods=['POST'])
def detect_language():
    """Detect if text is Vietnamese"""
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"error": "Missing text parameter"}), 400

    text = data['text']
    is_viet = is_vietnamese_text(text)

    vietnamese_chars = [c for c in text if c in VIETNAMESE_CHARACTERS]

    return jsonify({
        "text": text,
        "is_vietnamese": is_viet,
        "detected_language": "vietnamese" if is_viet else "unknown",
        "vietnamese_characters": vietnamese_chars,
        "vietnamese_char_count": len(vietnamese_chars),
        "confidence": len(vietnamese_chars) / len(text) if text else 0
    })

if __name__ == "__main__":
    app.run(debug=True)