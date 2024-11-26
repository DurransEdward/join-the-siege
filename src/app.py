from flask import Flask, request, jsonify
from src.classifier import classify_file
from src.config import *

app = Flask(__name__)

def allowed_file(file):
    return file.content_type in ALLOWED_CONTENT_TYPES # Checking the content_type instead of the file extension is more robust since is possible to have a mismatch between the file extension and the actual content.

@app.route('/classify_file', methods=['POST'])
def classify_file_route():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if not allowed_file(file):
        return jsonify({"error": "File type not allowed"}), 400

    file_class = classify_file(file, DOCUMENT_CLASSES, OPEN_AI_MODEL)
    return jsonify({"file_class": file_class}), 200

if __name__ == '__main__':
    app.run(debug=True)