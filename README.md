
# Dog Cat Classifier


This Dog Cat Classifier application is a simple web service built with Flask that allows users to upload images of dogs or cats. Upon uploading, the application saves the image and uses a trained convolutional neural network (CNN) to classify it as either a dog or a cat. The model provides a confidence score for its prediction, making it a useful tool for animal enthusiasts and developers alike to explore image classification technology.
## Run Locally

Install Python 3.10.0


  https://www.python.org/downloads/release/python-3100/

Install Node 21.6.2


  https://nodejs.org/en/blog/release/v21.6.2


Clone the project

```bash
  git clone https://github.com/chamoddissanayake/Dog-Cat-Classifier.git
```

Go to Frontend Folder

```bash
  Frontend > dog-cat-classifier
```

Install dependencies

```bash
  npm install
```

Start the Frontend

```bash
  npm start
```

Go to Frontend Web App

```bash
  http://localhost:3000/
```

Go to Backend Folder

```bash
  Backend >
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Start the Backend

```bash
  python app.py
```
## Tech Stack

**Backend :** Flask

**Frontend :** React

**Machine Learning Framework:** TensorFlow (with Keras)

**Image Processing:** Keras (for loading and preprocessing images)

**Storage:** Local filesystem (for uploading and storing images)

**API Communication:** Flask-RESTful (for defining RESTful endpoints)

**Development Environment:** Python

**Model Saving/Loading:** HDF5 (for saving and loading the Keras model)
## Usage/Examples


POST Method

```bash
http://127.0.0.1:5005/classify
```

Request
```javascript
Dog Image: 
{
    "image_path": "./imgs/pic11.jpg"
}

Cat Image:
{
    "image_path": "./imgs/img4.jpg"
}

```
Response
```javascript
Dog Image: 
{
    "confidence": 0.9979569911956787,
    "predictedState": "dog"
}

Cat Image:
{
    "confidence": 0.15947717428207397,
    "predictedState": "cat"
}

```
