import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

MODEL_PATH = 'model/cnn_model.h5'

def predict_image(image_path):
    # Load the model
    model = load_model(MODEL_PATH)

    # Load and preprocess the image
    img = image.load_img(image_path, target_size=(100, 100))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    
    # Predict
    prediction = model.predict(img_array)
    predicted_class = 'cat' if prediction < 0.5 else 'dog'
    confidence = prediction[0][0]
    
    return predicted_class, confidence
