import cv2
import mediapipe as mp
import pyautogui
from utils import set_volume, adjust_volume, play_pause_media, next_track, prev_track, is_pinch, smooth_cursor, is_dragging

# Function to track hand landmarks and control mouse and media with UI feedback
def track_hand_and_control(frame, hands, prev_x, prev_y, prev_finger_y, smooth_factor, prev_drag_position):
    h, w, _ = frame.shape
    # Convert the frame to RGB (required by MediaPipe)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    action_text = ""  # Variable to hold action text for UI feedback

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Get the tip of the index finger and thumb
            index_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            index_x, index_y = int(index_tip.x * w), int(index_tip.y * h)
            screen_x, screen_y = int(index_tip.x * screen_w), int(index_tip.y * screen_h)

            # Smooth cursor movement
            mouse_x, mouse_y = smooth_cursor(prev_x, prev_y, screen_x, screen_y, smooth_factor)
            pyautogui.moveTo(mouse_x, mouse_y)
            prev_x, prev_y = mouse_x, mouse_y

            # Detect pinch (distance between thumb and index finger)
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)

            if is_pinch(index_x, index_y, thumb_x, thumb_y):
                pyautogui.click()
                action_text = "Left Click"

                # Right click gesture: thumb and index finger spread
                if abs(index_x - thumb_x) > 50:
                    pyautogui.rightClick()
                    action_text = "Right Click"

            # Volume Control based on finger movement
            if prev_finger_y is not None:
                diff_y = prev_finger_y - screen_y
                if abs(diff_y) > 20:
                    if diff_y > 0:
                        adjust_volume(increase=True)
                        action_text = "Volume Up"
                    elif diff_y < 0:
                        adjust_volume(increase=False)
                        action_text = "Volume Down"

            prev_finger_y = screen_y

            # Media Player Controls
            if is_pinch(index_x, index_y, thumb_x, thumb_y):
                play_pause_media()
                action_text = "Play/Pause Media"

            if prev_x and (screen_x - prev_x) > 20:
                next_track()
                action_text = "Next Track"

            if prev_x and (screen_x - prev_x) < -20:
                prev_track()
                action_text = "Previous Track"

            # Drag and Drop functionality: Detecting pinch for dragging
            if is_dragging(index_x, index_y, thumb_x, thumb_y):
                if prev_drag_position is None:
                    prev_drag_position = (screen_x, screen_y)
                else:
                    pyautogui.moveTo(screen_x, screen_y)
                action_text = "Dragging..."

    # Display the action text as UI feedback
    cv2.putText(frame, action_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    return prev_x, prev_y, prev_finger_y, prev_drag_position

# Main function to run the virtual mouse gesture control
def main():
    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
    mp_draw = mp.solutions.drawing_utils

    # Initialize camera and get screen size
    cap = cv2.VideoCapture(0)
    screen_w, screen_h = pyautogui.size()

    prev_x, prev_y = 0, 0
    prev_finger_y = None
    prev_drag_position = None
    smooth_factor = 0.7

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)  # Flip frame horizontally for mirror effect

        prev_x, prev_y, prev_finger_y, prev_drag_position = track_hand_and_control(
            frame, hands, prev_x, prev_y, prev_finger_y, smooth_factor, prev_drag_position
        )

        # Display the webcam feed with action text
        cv2.imshow("Virtual Mouse", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()