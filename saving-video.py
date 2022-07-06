import cv2
from threading import Timer

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(
    '/home/pi/scripts/python-streaming-client/output.mp4', fourcc, 5.0, (640, 480))

flag = True


def switchFlag():
    global flag
    flag = False


timer = Timer(10, switchFlag)
timer.start()

while True:
    ret, frame = cap.read()

    out.write(frame)

    if not flag:
        break


cap.release()
out.release()
cv2.destroyAllWindows()
