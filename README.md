# SignaVision

A desktop sign-language interpretation demo built around the existing computer-vision model and webcam pipeline in this repository. The project keeps the original recognition workflow intact while presenting it in a more polished and presentation-ready interface.

## What the project does

- Live hand-sign recognition from the webcam
- Detects the supported classes in the current model: Hello, I love you, No, Okay, Please, Thank you, and Yes
- Displays the currently recognized sign in a polished UI panel
- Speaks the current sign output through the system speech engine
- Includes the existing eye-tracking demo as a secondary utility
- Provides a simple Windows launch script and a Tkinter-based desktop interface

## Project structure

- `Interface.py` — main SignaVision desktop application
- `test.py` — launcher for the main app
- `eyeTracker.py` — eye-tracking mouse utility
- `voiceRecognition.py` — microphone-based speech recognition sample
- `model/keras_model.h5` — trained sign-recognition model
- `model/labels.txt` — label mapping used by the classifier
- `Data/` — image samples used for dataset collection and reference

## Supported sign classes

The current model is trained for these labels:

- Hello
- I love you
- No
- Okay
- Please
- Thank you
- Yes

## Technologies used

- Python 3.11+
- Tkinter for the desktop UI
- OpenCV (`cv2`) for camera capture and image processing
- `cvzone` for hand detection and classification helpers
- TensorFlow / Keras model inference
- MediaPipe for the eye-tracking utility
- Windows SAPI or `pyttsx3` for speech output when available

## Setup

1. Open a terminal in the project folder.
2. Create and activate a virtual environment if desired:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install the project dependencies:

   ```powershell
   python -m pip install --upgrade pip
   python -m pip install opencv-python cvzone tensorflow mediapipe pyautogui SpeechRecognition pyaudio pillow pyttsx3
   ```

> `pyaudio` is required only when using the microphone-based speech recognition example in `voiceRecognition.py`.

## Launch the application

Use either of these commands from the project root:

```powershell
python Interface.py
```

or

```powershell
python test.py
```

On Windows, you can also run:

```powershell
.\run_app.bat
```

## Camera and model requirements

- The app expects webcam access on the local machine.
- If the camera is blocked or unavailable, the UI shows a clear error state instead of crashing.
- The trained model file must remain in `model/keras_model.h5` and the label file in `model/labels.txt`.
- The app is configured for the current single-hand sign-recognition workflow and does not claim continuous sentence translation or expanded gesture support.

## Notes

- The eye-tracking script uses a second webcam loop and should be launched intentionally as a separate utility.
- The sign detection workflow is intentionally kept close to the original code so the trained model and recognition behavior remain faithful to the project.
- The app is designed as a polished demonstration interface rather than a full rewrite of the recognition system.
