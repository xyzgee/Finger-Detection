# import necessary modules
import cv2
import mediapipe as mp
import pyautogui
import time

def count_fingers(lst):
    if lst is None:
        return 0
        
    cnt = 0
    
    # Single threshold for consistency
    threshold = 0.07
    
    # Thumb detection
    thumb_tip = lst.landmark[4]
    thumb_ip = lst.landmark[3]  # Using IP joint for thumb
    
    # Simple thumb detection
    if thumb_tip.x < thumb_ip.x - threshold:
        cnt += 1
        
    # Check fingers using pairs of tip and pip landmarks
    finger_pairs = [
        (8, 6),   # Index finger (tip, pip)
        (12, 10), # Middle finger (tip, pip)
        (16, 14), # Ring finger (tip, pip)
        (20, 18)  # Pinky finger (tip, pip)
    ]
    
    # Simple vertical comparison for each finger
    for tip_idx, pip_idx in finger_pairs:
        if lst.landmark[tip_idx].y < lst.landmark[pip_idx].y - threshold:
            cnt += 1
            
    return cnt

# Initialize video capture
cap = cv2.VideoCapture(0)

#intialize drawing utilities and hand models
mp_drawing = mp.solutions.drawing_utils #draw visual over the video
mp_hands = mp.solutions.hands
hand_obj = mp_hands.Hands(max_num_hands= 1) #giving maximum how many numbers it can detect

prev = -1
start_init = False

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)    # Flip the frame horizontally (mirror effect)
    
    # Convert the frame to RGB (MediaPipe uses RGB format)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the frame to detect hands
    results = hand_obj.process(rgb_frame)
    
    # If hands are detected, draw the landmarks
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            finger_count = count_fingers(hand_landmarks)
            
            if(prev!=finger_count):
                if not (start_init):
                    start_time = time.time()
                    start_init = True
                elif(time.time()-start_time)>0.2:
                    if(finger_count==1):
                        pyautogui.press('right')
                    elif(finger_count==2):
                        pyautogui.press('left')
                    elif(finger_count==3):
                        pyautogui.press('up')
                    elif(finger_count==4):
                        pyautogui.press('down')
                    elif(finger_count==5):
                        pyautogui.press('space')
                    
                    prev = finger_count
                    start_init = False
                    
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    else:
        finger_count = 0  # Default when no hand is detected
        
    # Display feedback on the screen
    cv2.putText(frame, f"Fingers: {prev}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Finger Detection GUI", frame)
    #imshow used to display the video or image
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

