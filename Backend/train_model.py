import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import load_model

MODEL_PATH = 'model/cnn_model.h5'

def build_model():
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(100, 100, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(32, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

def train_model():
    # Image data generator for loading images from 'data' folder
    train_datagen = ImageDataGenerator(rescale=1./255)
    train_generator = train_datagen.flow_from_directory(
        'data',
        target_size=(100, 100),
        batch_size=32,
        class_mode='binary'
    )
    
    model = build_model()
    model.fit(train_generator, epochs=5, batch_size=64)
    
    os.makedirs('model', exist_ok=True)
    model.save(MODEL_PATH)
    print("Model trained and saved.")

def check_and_train_model():
    if not os.path.exists(MODEL_PATH):
        print("Model not found, training model...")
        train_model()
    else:
        print("Model already trained.")
