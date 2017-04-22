import cv2
import time

cap = cv2.VideoCapture(0)

font = cv2.FONT_HERSHEY_SIMPLEX
currentFrameNumber = 1

t0 = time.time()

while(cap.isOpened()):
    ret, frame = cap.read()
    
    if ret == True:
        frame = cv2.flip(frame, 1)

        windowName = 'video-window'

        cv2.putText(frame, "%s frames" % str(currentFrameNumber), (10,30), font, 1, (200,0,0), 2)
        
        currentTimestamp = time.time()
        delta = currentTimestamp - t0
        cv2.putText(frame, "%s seconds" % ('%.2f' % delta), (10,60), font, 1, (200,210,0), 2)

        fps = currentFrameNumber / delta
        cv2.putText(frame, "%s fps" % ('%.2f' % fps), (10,90), font, 1, (0,200,0), 2)

        cv2.imshow(windowName, frame)     
        
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break
        
        currentFrameNumber = currentFrameNumber + 1
    else:
        break

cap.release()
cv2.destroyAllWindows()
