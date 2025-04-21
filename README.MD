# Virtual Mouse Gesture Control

A Python-based application that allows you to control your computer's mouse and media functions using hand gestures captured through your webcam.

## Features

Mouse Control:
- Mouse Movement: Control cursor position by moving your index finger in the air
- Left Click: Perform by pinching your thumb and index finger together
- Right Click: Perform by pinching and then spreading your thumb and index finger
- Drag and Drop: Enabled when maintaining a pinch gesture while moving

Volume Control:
- Volume Up: Move your hand upward
- Volume Down: Move your hand downward

Media Controls:
- Play/Pause: Quick pinch gesture
- Next Track: Swipe hand right
- Previous Track: Swipe hand left

Visual Feedback:
- Real-time FPS Counter: Displays current frames per second
- Action Display: Shows current gesture being performed
- Hand Tracking Visualization: Shows hand landmarks and connections
- On-screen Controls Guide: Displays all available commands

Additional Features:
- Smooth Cursor Movement: Implements cursor smoothing for precise control
- Gesture Recognition: Uses MediaPipe for accurate hand tracking
- Cross-platform Support: Works on both Windows and macOS
- Configurable Settings: Adjustable sensitivity and smoothing factors

## Requirements

Software Requirements:
- Python 3.10 or higher
- OpenCV (cv2) for image processing and webcam interface
- MediaPipe for hand tracking and gesture recognition
- PyAutoGUI for mouse and keyboard control
- Additional libraries specified in requirements.txt

Hardware Requirements:
- Webcam with minimum 720p resolution (1080p recommended)
- Processor: Intel Core i5/AMD Ryzen 5 or better
- RAM: 4GB minimum (8GB recommended)
- Well-lit environment for optimal hand tracking

System-Specific Requirements:

Windows:
- Administrative privileges for volume control
- Windows Media API support
- DirectX compatible graphics driver
- Windows 10 or higher recommended

macOS:
- macOS 10.15 (Catalina) or higher
- System Preferences access for:
  - Security & Privacy permissions
  - Accessibility control
  - Camera access
  - Screen recording permissions
  - System audio control

## Installation

1. Environment Setup:
   ```bash
   # Clone the repository
   git clone https://github.com/yourusername/virtual-mouse-gesture-control.git
   cd virtual-mouse-gesture-control

   # Create and activate virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   .\venv\Scripts\activate  # On Windows
   ```

2. Install Dependencies:
   ```bash
   # Install all required packages
   pip install -r requirements.txt
   ```

3. System Permissions:
   - macOS users: Grant permissions when prompted for:
     - Camera access
     - Accessibility features
     - Screen recording
     - System events control
   - Windows users: Run as administrator for first use

## Usage

1. Starting the Application:
   ```bash
   # Activate virtual environment if used
   source venv/bin/activate  # macOS/Linux
   # or
   .\venv\Scripts\activate   # Windows

   # Run the application
   python main.py
   ```

2. Optimal Setup:
   - Position your webcam at eye level
   - Ensure uniform lighting without strong backlighting
   - Maintain 20-50 cm distance from camera
   - Clear background for better hand detection

3. Gesture Controls:

   Mouse Functions:
   - Cursor Movement: Hold index finger up and move
   - Left Click: Quick pinch gesture
   - Right Click: Pinch and spread fingers
   - Drag and Drop: Hold pinch while moving

   System Controls:
   - Volume Adjustment: Move hand up/down
   - Media Playback: Pinch to play/pause
   - Track Navigation: Swipe left/right

4. Interface Elements:
   - Top-left: FPS counter
   - Center-left: Controls guide
   - Center: Action feedback
   - Main view: Hand tracking visualization

5. Exiting:
   - Press 'q' to quit
   - Or close the window

## Troubleshooting Guide

Common Issues and Solutions:

1. Hand Detection Problems:
   - Ensure adequate lighting (avoid dark or overly bright conditions)
   - Keep hands within camera frame
   - Avoid rapid movements
   - Check for objects obstructing hand view

2. Performance Issues:
   - Close resource-intensive applications
   - Check CPU/RAM usage
   - Reduce camera resolution if needed
   - Verify graphics drivers are updated

3. System Control Issues:
   - macOS:
     - Check Security & Privacy settings
     - Restart application after granting permissions
     - Verify audio device connectivity
   - Windows:
     - Run as administrator
     - Check Windows audio services
     - Verify media key functionality

4. Camera Issues:
   - Ensure no other applications are using the camera
   - Check USB connection if using external webcam
   - Verify camera drivers are up to date
   - Try different USB ports

5. Installation Problems:
   - Update pip: `pip install --upgrade pip`
   - Install individual packages if bulk install fails
   - Check Python version compatibility
   - Verify virtual environment activation

For persistent issues:
1. Check the error log in terminal
2. Verify all dependencies are correctly installed
3. Consider reinstalling the application
4. Submit an issue on the GitHub repository

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
