import pyautogui
import screeninfo
import math
import subprocess
import os
import numpy as np
from platform import system

# Determine the operating system
SYSTEM = system()

# Import OS-specific modules
if SYSTEM == "Windows":
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    # Initialize audio controller for Windows
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

# Function to set volume to a specific level
def set_volume(level):
    level = max(0, min(100, level))  # Clamp between 0 and 100
    if SYSTEM == "Windows":
        volume.SetMasterVolumeLevelScalar(level / 100, None)
    else:  # macOS
        os.system(f"osascript -e 'set volume output volume {level}'")

# Function to get current volume level
def get_volume():
    try:
        if SYSTEM == "Windows":
            return int(volume.GetMasterVolumeLevelScalar() * 100)
        else:  # macOS
            cmd = "osascript -e 'output volume of (get volume settings)'"
            return int(subprocess.check_output(cmd, shell=True))
    except:
        return 50  # Default volume if command fails

# Function to adjust volume based on the gesture movement
def adjust_volume(increase=True):
    current_volume = get_volume()
    
    # Increase or decrease volume by 5
    new_volume = current_volume + 5 if increase else current_volume - 5
    new_volume = max(0, min(100, new_volume))  # Clamp between 0 and 100
    set_volume(new_volume)

# Function to play or pause media
def play_pause_media():
    if SYSTEM == "Windows":
        pyautogui.press('playpause')
    else:  # macOS
        os.system("""osascript -e 'tell application "System Events" to key code 49'""")  # space key

# Function to go to the next media track
def next_track():
    if SYSTEM == "Windows":
        pyautogui.press('nexttrack')
    else:  # macOS
        os.system("""osascript -e 'tell application "System Events" to key code 124 using {command down}'""")  # right arrow

# Function to go to the previous media track
def prev_track():
    if SYSTEM == "Windows":
        pyautogui.press('prevtrack')
    else:  # macOS
        os.system("""osascript -e 'tell application "System Events" to key code 123 using {command down}'""")  # left arrow

# Function to check if a pinch gesture is detected (thumb and index finger close)
def is_pinch(index_x, index_y, thumb_x, thumb_y):
    distance = math.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)
    return distance < 30  # Adjust distance threshold as necessary

# Function to check if the user is dragging (thumb and index finger spread)
def is_dragging(index_x, index_y, thumb_x, thumb_y):
    distance = math.sqrt((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2)
    return distance > 60  # Dragging gesture when the distance is greater than a threshold

# Function to smooth cursor movement
def smooth_cursor(prev_x, prev_y, curr_x, curr_y, smooth_factor=0.7):
    # Smooth the cursor movement by gradually adjusting to the target position
    smooth_x = prev_x + (curr_x - prev_x) * smooth_factor
    smooth_y = prev_y + (curr_y - prev_y) * smooth_factor
    return int(smooth_x), int(smooth_y)

# Function to get screen resolution (useful if needed for customization)
def get_screen_resolution():
    screen = screeninfo.get_monitors()[0]
    return screen.width, screen.height