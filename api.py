from flask import Flask, request, jsonify
from flask_cors import CORS
import unicodedata
from app import style_text, add_diacritics, STYLE_CONFIG, COMBINING_MARKS

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

if __name__ == "__main__":
    app.run(debug=True)