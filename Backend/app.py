import os
import time
from flask import Flask, request, send_from_directory, jsonify
from predict import predict_image
from train_model import check_and_train_model
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Folder to store uploaded images
UPLOAD_FOLDER = './uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/uploads/<path:filename>', methods=['GET'])
def serve_image(filename):
    # Use send_from_directory to serve the image file
    return send_from_directory(UPLOAD_FOLDER, filename)

# Create the uploads folder if it doesn't exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


# Check if model is trained, if not, train it
check_and_train_model()

# Helper function to get file extension
def get_file_extension(filename):
    return os.path.splitext(filename)[1]

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Get the file extension from the original file
    file_extension = get_file_extension(file.filename)
    
    # Refactor the file name to the current epoch time with original extension
    epoch_time = int(time.time())
    filename = f"{epoch_time}{file_extension}"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    return jsonify({"image_path": file_path}), 200


@app.route('/classify', methods=['POST'])
def classify_image():
    data = request.json
    image_path = data.get('image_path')
    
    if not image_path:
        return jsonify({"error": "No image path provided"}), 400

    prediction, confidence = predict_image(image_path)
    
    return jsonify({"predictedState": prediction, "confidence": float(confidence)})

if __name__ == '__main__':
    app.run(debug=True, port=5005)
