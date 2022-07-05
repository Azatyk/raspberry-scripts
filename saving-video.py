# organize imports
import cv2
from threading import Timer

# This will return video from the first webcam on your computer.
cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter(
    '/home/pi/scripts/python-streaming-client/output.mp4', fourcc, 20.0, (640, 480))

flag = True


def switchFlag():
    global flag
    flag = False


timer = Timer(15, switchFlag)

# loop runs if capturing has been initialized.
while True:
    # reads frames from a camera
    # ret checks return at each frame
    ret, frame = cap.read()

    # output the frame
    out.write(frame)

    if not flag:
        break


# Close the window / Release webcam
cap.release()

# After we release our webcam, we also release the output
out.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
