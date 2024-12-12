# import necessary modules
import cv2
import mediapipe as mp
import pyautogui
import time

def count_fingers(lst):
    cnt= 0 #intialize count is 0
    #calculating the threshold value
    # it is fixed because base of the hand to center point of the hand and also not the tip because it wont be accurate
    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2 # calculating the distance between the 0 to the first finger(middle) starting pt *100 because the value will be of 0 to 1 to make it for 100 for calculation
    
    #first four fingers
    if(lst.landmark[5].y*100 - lst.landmark[8].y*100)> thresh:
        cnt +=1
    if(lst.landmark[9].y*100 - lst.landmark[12].y*100)> thresh:
        cnt +=1
    if(lst.landmark[13].y*100 - lst.landmark[16].y*100)> thresh:
        cnt +=1
    if(lst.landmark[17].y*100 - lst.landmark[20].y*100)> thresh:
        cnt +=1
    
    #for thumb we taking x axis bcs it moves in other direction
    if(lst.landmark[5].x*100 - lst.landmark[4].x*100)> 5: #using a fixed approch can be used as thresh too but more complexity
        cnt +=1
    return cnt

#capture from webcam to capture video from webcam the value is 0
cap = cv2.VideoCapture(0)

#intialize drawing utilities and hand models
mp_drawing = mp.solutions.drawing_utils #draw visual over the video
mp_hands = mp.solutions.hands
hand_obj = mp_hands.Hands(max_num_hands= 1) #giving maximum how many numbers it can detect

prev = -1
start_init = False

#loop through each frame of the video
while True:
    end_time = time.time()
    ret, frame = cap.read()#ret is return of bool values and frame is going to capture the video
    frame = cv2.flip(frame, 1)    # Flip the frame horizontally (mirror effect)
    
    # Convert the frame to RGB (MediaPipe uses RGB format)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Process the frame to detect hands
    results = hand_obj.process(rgb_frame)
    
    # If hands are detected, draw the landmarks
    if results.multi_hand_landmarks:
        hand_landmarks = results.multi_hand_landmarks[0]  # Access the first hand
        count= count_fingers(hand_landmarks) #calling function to count number of fingers using the hand landmarks
        # print(count)
        if(prev!=count):
            if not (start_init):
                start_time = time.time()
                start_init = True
            elif(end_time-start_time)>0.2:

                if(count==1):
                    pyautogui.press('right') #press right if one finger is shown
                
                elif(count==2):
                    pyautogui.press('left') #press left if 2 finger raised
                
                elif(count==3):
                    pyautogui.press('up') #press up if 3 finger raised
                
                elif(count==4):
                    pyautogui.press('down') #press down if 4 finger raised
                
                elif(count==5):
                    pyautogui.press('space') #press space if 5 finger raised
                
                prev= count
                start_init= False
        mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
    # Display feedback on the screen
    cv2.putText(frame, f"Fingers: {prev}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("My Webcam", frame)
    cv2.imshow("My Webcam", frame)#imshow used to display the video or image
    
    if cv2.waitKey(1) == 27: #after 1 milliesecond of the esc is clicked it should perform the following
        cv2.destroyAllWindows()
        cap.release()
        break

#Done by J. N. Ravinandan