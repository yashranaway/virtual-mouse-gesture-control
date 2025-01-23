# Virtual Mouse Gesture Control

This project enables you to control the mouse, adjust system volume, and manage media playback (play/pause, next/previous track) using hand gestures via a webcam. It uses **OpenCV** for hand tracking and **MediaPipe** for detecting hand landmarks.

## Features
- Control mouse cursor with index finger gestures.
- Adjust system volume with swipe gestures.
- Play, pause, skip, and go back on media players with gestures.

## Requirements
- Python 3.x
- opencv-python
- mediapipe
- pyautogui

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/virtual-mouse-gesture-control.git
    ```
2. Navigate to the project directory:
    ```bash
    cd virtual-mouse-gesture-control
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the application:
    ```bash
    python main.py
    ```

## Usage
- Ensure your webcam is connected and working.
- Follow the on-screen instructions to perform gestures for controlling the mouse, volume, and media playback.

## License
This project is licensed under the MIT License. See the [LICENSE] file for more details.