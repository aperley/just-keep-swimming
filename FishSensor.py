import numpy as np
import cv2
from DataTypes import FishPosition

class FishSensor(object):
    def __init__(self):
	    self.cap = cv2.VideoCapture(0)
	    self.cap.set(3, 280)
	    self.cap.set(4, 192)

	    cv2.namedWindow("image")

	    lower_b, lower_g, lower_r = 0, 0, 80
	    upper_b, upper_g, upper_r = 130, 75, 115
	    self.lower = np.array([lower_b, lower_g, lower_r], dtype='uint8')
	    self.upper = np.array([upper_b, upper_g, upper_r], dtype='uint8')

    def poll(self):
        ret, frame = self.cap.read()
        mask = cv2.inRange(frame, self.lower, self.upper)

	idx_rows, idx_cols = np.where(mask)
	if len(idx_rows > 0):
		row = int(round(idx_rows.mean()))
		col = int(round(idx_cols.mean()))
		marked_frame = cv2.circle(frame, (col, row), 5, (0, 0, 255), -1)

	cv2.imshow("image", frame)
	key = cv2.waitKey(1)
	return FishPosition(x=float(col)/(280/2)-1.0, y=float(row)/(192/2)-1.0)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    cap.set(3, 280)
    cap.set(4, 192)

    def onClick(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print x, y, frame[y, x]

    cv2.namedWindow("image")
    cv2.setMouseCallback("image", onClick)

    lower_b, lower_g, lower_r = 0, 0, 80
    upper_b, upper_g, upper_r = 130, 75, 115
    mode = 0

    while True:
        ret, frame = cap.read()
        lower = np.array([lower_b, lower_g, lower_r], dtype='uint8')
        upper = np.array([upper_b, upper_g, upper_r], dtype='uint8')
        mask = cv2.inRange(frame, lower, upper)

	idx_rows, idx_cols = np.where(mask)
	if len(idx_rows > 0):
		row = int(round(idx_rows.mean()))
		col = int(round(idx_cols.mean()))
		marked_frame = cv2.circle(frame, (col, row), 5, (0, 0, 255), -1)
		#cv2.imshow("image", marked_frame)
	else:
		pass
		#cv2.imshow("image", frame)
	
	if mode:
		output = cv2.bitwise_and(frame, frame, mask=mask)
		cv2.imshow("image", output)
	else:
		cv2.imshow("image", frame)

	key = cv2.waitKey(1)
	if key & 0xFF == ord('q'):
		break
	if key & 0xFF == ord('w'):
		lower_b += 5
	if key & 0xFF == ord('s'):
		lower_b -= 5
	if key & 0xFF == ord('e'):
		lower_g += 5
	if key & 0xFF == ord('d'):
		lower_g -= 5
	if key & 0xFF == ord('r'):
		lower_r += 5
	if key & 0xFF == ord('f'):
		lower_r -= 5
	if key & 0xFF == ord('t'):
		upper_b += 5
	if key & 0xFF == ord('g'):
		upper_b -= 5
	if key & 0xFF == ord('y'):
		upper_g += 5
	if key & 0xFF == ord('h'):
		upper_g -= 5
	if key & 0xFF == ord('u'):
		upper_r += 5
	if key & 0xFF == ord('j'):
		upper_r -= 5
	if key & 0xFF == ord('m'):
		mode = 1 if mode == 0 else 0
	if ord('a') <= (key & 0xFF) <= ord('z'):
		print (lower_b, lower_g, lower_r), (upper_b, upper_g, upper_r)

    cap.release()
    cv2.destroyAllWindows()
