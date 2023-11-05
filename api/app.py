import pytesseract
from PIL import Image
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/' , methods=['POST'])
def extract_text():
    try:
        uploaded_image = request.files['image']
        if uploaded_image:
            image = Image.open(uploaded_image)
            languages = "eng+amh"
            text = pytesseract.image_to_string(image, lang=languages)
            # Check if the extracted text is empty
            if not text.strip():
                return 'No text detected, please upload image with text!'
            
            # Split the text into lines using a dot (.) as the delimiter
            lines = text.split('.')
            
            # Join the lines with newline characters to create a new line for each sentence
            cleaned_text = '\n'.join(lines).strip()

            return cleaned_text
    except Exception as e:
        return jsonify({'error': 'Error processing the image.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
