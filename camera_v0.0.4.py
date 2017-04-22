import cv2

cap = cv2.VideoCapture(0)

pressedKey = 1
font = cv2.FONT_HERSHEY_SIMPLEX

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        frame = cv2.flip(frame, 1)

        windowName = ':SnapChat:'

        ch = cv2.waitKey(1)
        if ch == ord('1'):
            pressedKey = 1            
        elif ch == ord('2'):
            pressedKey = 2            
        elif ch == ord('3'):
            pressedKey = 3            
        elif ch == ord('4'):
            pressedKey = 4
        elif ch == ord('5'):
            pressedKey = 5            
        elif ch == ord('6'):
            pressedKey = 6
        elif ch == ord('7'):
            pressedKey = 7            
        elif ch == ord('8'):
            pressedKey = 8
        elif ch == ord('9'):
            pressedKey = 9   
        elif ch == ord('x'):            
            break
            
        cv2.putText(frame, str(pressedKey), (320,60), font, 2, (100,40,90), 2)
        
        cv2.imshow(windowName, frame)
    else:
        break

cap.release()
cv2.destroyAllWindows()
