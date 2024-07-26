import os
import logging
from flask import Flask, request, render_template, redirect, url_for, send_from_directory
from paddleocr import PaddleOCR

# Initialize Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}

# Disable debug logs from PaddleOCR
logging.getLogger('ppocr').setLevel(logging.WARNING)

# Initialize the PaddleOCR model with CPU configuration
ocr = PaddleOCR(use_angle_cls=True, lang='en')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # If user does not select file, browser also submits an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = file.filename
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            try:
                # Perform OCR on the uploaded image
                result = ocr.ocr(filepath, cls=True)
                # Extract the full text
                full_text = " ".join(line[1][0] for res in result for line in res)
                return render_template('index.html', text=full_text, image_path=url_for('static', filename=f'uploads/{filename}'))
            except Exception as e:
                logging.error(f"An error occurred: {str(e)}")
                return render_template('index.html', error=str(e))

    return render_template('index.html')

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
