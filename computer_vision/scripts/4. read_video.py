import numpy as np
import cv2

video_capture = cv2.VideoCapture(0)
# video_capture = cv2.VideoCapture($PATH)

while(True):
    ret, frame = video_capture.read()

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()