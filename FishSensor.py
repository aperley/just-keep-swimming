import numpy as np
import cv2
from DataTypes import FishPosition

class FishSensor(object):
    def __init__(self):
        pass

    def poll(self):
        return FishPosition(x=0, y=0)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    def onClick(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print x, y, frame[y, x]

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", onClick)

    while True:
        ret, frame = cap.read()
        lower = np.array([0, 65, 130], dtype='uint8')
        upper = np.array([40, 120, 200], dtype='uint8')
        mask = cv2.inRange(frame, lower, upper)
        output = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("image", output)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()