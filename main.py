import cv2
import mediapipe as mp
import numpy as np

# Mediapipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
canvas = None
prev_x, prev_y = 0, 0


def fingers_up(handLms):
    tips = [8, 12, 16, 20]  
    fingers = []
    for tip in tips:
        if handLms.landmark[tip].y < handLms.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers


def hand_distance(handLms):
 
    x1, y1 = handLms.landmark[4].x, handLms.landmark[4].y
    x2, y2 = handLms.landmark[8].x, handLms.landmark[8].y
    return np.sqrt((x2 - x1)**2 + (y2 - y1)**2)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    if canvas is None:
        canvas = np.zeros_like(img)

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

           
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            fingers = fingers_up(handLms)
            x = int(handLms.landmark[8].x * img.shape[1])
            y = int(handLms.landmark[8].y * img.shape[0])
            dist = hand_distance(handLms)

            
            if fingers == [1, 0, 0, 0] and dist > 0.05:  
                if prev_x == 0 and prev_y == 0:
                    prev_x, prev_y = x, y
                cv2.line(canvas, (prev_x, prev_y), (x, y), (0, 215, 255), 8)
                prev_x, prev_y = x, y

           
            elif fingers == [1, 1, 1, 1]:
                cv2.circle(canvas, (x, y), 50, (0, 0, 0), -1)
                prev_x, prev_y = 0, 0

            else:
                prev_x, prev_y = 0, 0

 
    img_gray = cv2.cvtColor(canvas, cv2.COLOR_BGR2GRAY)
    _, img_inv = cv2.threshold(img_gray, 20, 255, cv2.THRESH_BINARY_INV)
    img_inv = cv2.cvtColor(img_inv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, img_inv)
    img = cv2.bitwise_or(img, canvas)

    cv2.imshow("Golden Pen + Hand Points ✨", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
