# RPI производит socket connection через socket.io
# RPI ждет сообщения об сканировании QR через socket.io
# RPI включает запись видео через openCV
# RPI открывает замок через GPIO на определенное время используя time и закрывает
# RPI отправляет сообщение о том, что холодильник открыт
# RPI смотрит значения датчика холла и отправляет сообщение о закрытии холодильника, когда он закрывается
# RPI заканчивает запись видео и сохраняет видео локально
# RPI post запросом отправляет видео на сервер

import socketio
import RPi.GPIO as GPIO
import time

sio = socketio.Client()

# GPIO setting locket pin and pin mode
locketPin = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(locketPin, GPIO.OUT)

# socket.io events
socketEvents = {
    "qr_scanned": "qr_scanned",
}

socketEmits = {
    "locker_opened": "locker_opened",
    "locker_closed": "locker_closed",
    "locker_opening_error": "locker_opening_error",
}


def message(message):
    print("-------------------")
    print(message)
    print("-------------------")


@sio.event
def connect():
    message("Connected to server")


@sio.event
def qr_scanned():
    # try:
    GPIO.output(locketPin, True)
    sio.emit(socketEmits["locker_opened"])
    message("Locker opened")

    time.sleep(10)
    GPIO.output(locketPin, False)
    sio.emit(socketEmits["locker_closed"])
    message("Locker closed")
    # except:
    #     sio.emit(socketEmits["locker_opening_error"])
    #     message("Error on opening locker")


@sio.event
def disconnect():
    message("Disconnected from server")


# socket.io connection to server
sio.connect('http://192.168.187.179:3002')


sio.wait()
