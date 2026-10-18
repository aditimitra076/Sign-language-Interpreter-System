# Sign Language Interpreter System

A Python-based computer vision project that explores sign language recognition, speech recognition, and eye tracking through separate interactive applications.

## Features

- **Sign Language Recognition:** Uses a trained machine learning model and webcam-based hand tracking to recognize supported hand gestures.
- **Speech Recognition:** Provides a separate speech recognition module.
- **Eye Tracking:** Uses computer vision to track eye movements through a separate module.
- **Desktop Interface:** A simple Tkinter launcher provides access to the available features.

## Technologies Used

- Python
- OpenCV
- TensorFlow / Keras
- cvzone
- Tkinter
- NumPy
- Speech recognition and eye-tracking libraries used by the respective modules

## Project Structure

```text
signLanguageDetection/
├── Interface.py
├── test.py
├── dataCollection.py
├── eyeTracker.py
├── voiceRecognition.py
├── keras_model.h5
├── Data.zip
├── requirements.txt
├── run_app.bat
└── README.md
```

*Note: The project structure may vary depending on the local model and dataset files.*

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aditimitra076/Sign-language-Interpreter-System.git
cd Sign-language-Interpreter-System
```

### 2. Create a virtual environment (recommended)

```bash
python -m venv venv
```

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If a dependency is missing, install the required package compatible with your Python version and existing model.

### 4. Run the application

```bash
python Interface.py
```

The launcher provides access to the sign language interpreter, speech recognition, and eye-tracking modules.

## How It Works

The sign recognition module uses a webcam to capture hand gestures and a trained model to classify supported signs. The speech recognition and eye-tracking functionalities are implemented in separate Python modules.

The available functionality depends on the installed dependencies, model files, camera access, and the configuration of each module.

## Requirements

- Python installed on your system
- A webcam for sign recognition and eye tracking
- The required trained model and any associated label files
- Dependencies listed in `requirements.txt`
- Microphone access for speech recognition, where required

## Future Improvements

- Improve the desktop interface and usability.
- Expand the supported gesture vocabulary.
- Improve recognition accuracy and robustness.
- Integrate the individual modules into a more cohesive application.
- Improve accessibility and user feedback.

## Author

**Aditi Mitra**

- GitHub: [@aditimitra076](https://github.com/aditimitra076)

## Disclaimer

This project is intended for educational and demonstration purposes. Its recognition capabilities are limited to the gestures and functionalities implemented in the current codebase.