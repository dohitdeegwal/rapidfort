import os
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename
import mimetypes

#  log the request and response
import logging
logging.basicConfig(level=logging.DEBUG)


app = Flask(__name__)

# Define the directory where uploaded files will be temporarily stored
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Define the directory for static assets (CSS, JavaScript, etc.)
STATIC_FOLDER = 'public'
app.config['STATIC_FOLDER'] = STATIC_FOLDER

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to extract file metadata
def extract_metadata(file_path):
    try:

        # Use mimetypes module to parse MIME type and get additional information
        mime_details = mimetypes.guess_type(file_path)

        metadata = {
            'File Name': os.path.basename(file_path),
            'File Type': mime_details,  # Include MIME type details
        }

        return metadata
    except Exception as e:
        print(e)
        return {"Error": "Unable to extract metadata."}

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"Error": "No file part"})

    uploaded_file = request.files['file']
    
    if uploaded_file.filename == '':
        return jsonify({"Error": "No selected file"})

    if uploaded_file:
        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(file_path)

        # Extract metadata from the uploaded file
        metadata = extract_metadata(file_path)

        # Remove the uploaded file after extracting metadata
        os.remove(file_path)

        return jsonify(metadata)

# Serve static files from the 'public' folder
@app.route('/public/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.config['STATIC_FOLDER'], filename)

if __name__ == '__main__':
    # run on on port 5000
    app.run(debug=True, port=5000, host='0.0.0.0')