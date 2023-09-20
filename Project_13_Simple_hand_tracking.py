#Import the necessary Packages 
import mediapipe
import cv2

#Use MediaPipe to draw the hand framework over the top of hands it identifies in Real-Time
drawingModule = mediapipe.solutions.drawing_utils
handsModule = mediapipe.solutions.hands

#Use CV2 Functionality to create a Video stream and add some values
cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')


with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=2) as hands:

#Create an infinite loop which will produce the live feed to our desktop and that will search for hands
     while True:
           ret, frame = cap.read()
           frame1 = cv2.resize(frame, (640, 480))
           results = hands.process(cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB))
        
           if results.multi_hand_landmarks != None:
              for handLandmarks in results.multi_hand_landmarks:
                  drawingModule.draw_landmarks(frame1, handLandmarks, handsModule.HAND_CONNECTIONS)
                  

           cv2.imshow("Frame", frame1);
           key = cv2.waitKey(1) & 0xFF
           
           if key == ord("q"):
              break

