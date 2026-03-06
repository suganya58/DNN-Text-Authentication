# Document Authenticity Detector

## Overview
The Document Authenticity Detector is a machine learning-based system that verifies whether a document or text content is authentic or suspicious. The system analyzes textual features and predicts the authenticity of the document using a trained classification model.

The project includes a simple web-based interface where users can input document text and receive an instant prediction result.

## Features
- Detects whether a document is authentic or suspicious
- Machine learning-based text classification
- Simple and user-friendly web interface
- Real-time prediction results
- Easy to retrain the model with new datasets

## Technologies Used
- Python
- Flask
- HTML
- Scikit-learn
- Pandas
- NumPy

## Project Structure
Document-Authenticity-Detector/
│
├── app.py
├── index.html
├── result.html
├── prepared_dataset.py
├── train_text_classifier.py
└── README.md

## Installation

1. Clone the repository

git clone https://github.com/your-username/document-authenticity-detector.git

2. Navigate to the project directory

cd document-authenticity-detector

3. Install required dependencies

pip install -r requirements.txt

## Running the Project

1. Train the machine learning model

python train_text_classifier.py

2. Run the Flask application

python app.py

3. Open your browser and go to

http://127.0.0.1:5000/

## How It Works
1. The dataset is cleaned and prepared using prepared_dataset.py.
2. The model is trained using train_text_classifier.py.
3. The trained model is integrated into the Flask web application.
4. Users enter document text in the web interface.
5. The system analyzes the text and predicts whether the document is authentic or suspicious.

## Future Improvements
- Improve prediction accuracy with larger datasets
- Add deep learning-based detection
- Support document uploads (PDF, DOCX)
- Improve the user interface

## Author
Suganya S
