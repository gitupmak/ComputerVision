# Aslam Khan
import cv2
while True:
    cap = cv2.VideoCapture(0)
    check,frame = cap.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()