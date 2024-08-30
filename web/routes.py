from flask import render_template, request, jsonify
from PIL import Image
from io import BytesIO
import base64
import pytesseract

def configure_routes(app):
    
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/process-image', methods=['POST'])
    def process_image():
        data = request.json
        image_data = data['image'].split(",")[1]
        image_bytes = base64.b64decode(image_data)
        image = Image.open(BytesIO(image_bytes))
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        text = pytesseract.image_to_string(image, lang='por')

        return jsonify({'text': text})
