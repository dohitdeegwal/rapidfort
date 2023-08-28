import os
from flask import render_template, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from app import app
from metadata import extract_metadata

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
        return jsonify({"Error": "No file part"})

    uploaded_file = request.files["file"]

    if uploaded_file.filename == "":
        return jsonify({"Error": "No selected file"})

    if uploaded_file:
        filename = secure_filename(uploaded_file.filename)
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        uploaded_file.save(file_path)

        metadata = extract_metadata(file_path)

        os.remove(file_path)

        return jsonify(metadata)

@app.route("/public/<path:filename>")
def serve_static(filename):
    return send_from_directory(app.config["STATIC_FOLDER"], filename)
