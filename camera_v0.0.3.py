import turtle
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')

#fereastra mica calculator
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

#smmartphone
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (480,800))

#test
#out = cv2.VideoWriter('output.avi',fourcc, 20.0, (1080,1080))

#test_2
out = cv2.VideoWriter('output.avi',fourcc, 65535, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)

        
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
