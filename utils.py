import os
import pyautogui


# Volume Control Utilities
def set_volume(volume_level):
    """Set system volume to a specified level."""
    try:
        os.system(f"osascript -e 'set volume output volume {volume_level}'")
    except Exception as e:
        print(f"Error setting volume: {e}")


def adjust_volume(increase=True, step=5):
    """Adjust the system volume by a specified step."""
    try:
        current_volume = int(os.popen("osascript -e 'output volume of (get volume settings)'").read())
        new_volume = min(current_volume + step, 100) if increase else max(current_volume - step, 0)
        set_volume(new_volume)
        return new_volume
    except Exception as e:
        print(f"Error adjusting volume: {e}")
        return current_volume


# Media Control Utilities
def play_pause_media():
    """Play or pause the media player."""
    try:
        os.system("osascript -e 'tell application \"System Events\" to keystroke \" \" using command down'")
    except Exception as e:
        print(f"Error in media play/pause: {e}")


def next_track():
    """Skip to the next media track."""
    try:
        os.system("osascript -e 'tell application \"System Events\" to keystroke \"n\" using command down'")
    except Exception as e:
        print(f"Error going to next track: {e}")


def prev_track():
    """Go to the previous media track."""
    try:
        os.system("osascript -e 'tell application \"System Events\" to keystroke \"p\" using command down'")
    except Exception as e:
        print(f"Error going to previous track: {e}")


# Gesture Detection Utilities
def is_pinch(index_x, index_y, thumb_x, thumb_y, threshold=30):
    """Detect if a pinch gesture is performed based on the distance between thumb and index finger."""
    distance = ((index_x - thumb_x) ** 2 + (index_y - thumb_y) ** 2) ** 0.5
    return distance < threshold


def smooth_cursor(prev_x, prev_y, screen_x, screen_y, smooth_factor=0.7):
    """Smooth the cursor movement using a weighted average of previous and current positions."""
    mouse_x = int(smooth_factor * prev_x + (1 - smooth_factor) * screen_x)
    mouse_y = int(smooth_factor * prev_y + (1 - smooth_factor) * screen_y)
    return mouse_x, mouse_y