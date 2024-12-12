# Gesture Media Controller

## Overview
This Python project allows you to control media applications using hand gestures, detected through a webcam. By using hand gestures, you can simulate pressing keys like "right", "left", "up", "down", and "space". The project uses the MediaPipe library to detect hand landmarks and the pyautogui library to simulate keypresses.

## Features
- Detects hand gestures through webcam input.
- Recognizes up to 5 distinct hand gestures (fingers raised).
- Simulates keyboard input based on the number of fingers raised:
  - 1 finger → "right" key press
  - 2 fingers → "left" key press
  - 3 fingers → "up" key press
  - 4 fingers → "down" key press
  - 5 fingers → "space" key press

## Prerequisites
- Python 3.7 or higher.
- Webcam.

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Dependencies:
- `opencv-python`
- `mediapipe`
- `pyautogui`

## Usage
1. Run the program:
   ```bash
   python gesture_media_controller.py
   ```
   - Simply raise your fingers in front of the webcam to trigger different key presses based on the number of fingers.
   - The program will continuously process frames from the webcam, and the corresponding key will be pressed based on the detected gesture.
   - Press `Esc` to exit the program.

2. Perform gestures in front of the webcam to trigger actions:
   - **1 Finger**: Left Arrow.
   - **2 Fingers**: Right Arrow.
   - **3 Fingers**: Up Arrow.
   - **4 Fingers**: Down Arrow.
   - **5 Fingers**: Spacebar.

3. Press `ESC` to exit.

## Files in this Repository
- `gesture_media_controller.py`: The main Python script that detects hand gestures and simulates key presses to control media.
- `requirements.txt`: A text file containing all the Python libraries required to run the project.
- `hand_landmarks_image.png`: An image showing the hand landmarks used in the gesture detection process.

## Output

![output](https://github.com/user-attachments/assets/292db8c6-7936-4662-be1b-18bc55c1514d)


## Troubleshooting
- Ensure your webcam is functional.
- Proper lighting improves detection accuracy.
- Address MediaPipe file issues by ensuring all required files are installed.

## Customization
- Adjust debounce timing in the script for response delay.
- Extend the `count_fingers` function for additional gestures.

## Future Enhancements
- Add support for more complex gestures.
- Introduce feedback through sound or on-screen indicators.

---

**Done By:** [@Ravinandan2005](https://github.com/ravinandan2005)
