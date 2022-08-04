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
locketPin = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(locketPin, GPIO.OUT)

# socket.io events
socketEvents = {
    "qr_scanned": "qr_scanned",
}

socketEmits = {
    "locker_opened": "locket_opened",
    "locket_closed": "locket_closed",
    "locket_opening_error": "locket_opening_error",
}


@sio.event
def connect():
    print('connection established')


@sio.on(socketEvents["qr_scanned"])
def on_qr_scanned():
    try:
        GPIO.output(locketPin, True)
        sio.emit(socketEmits["locker_opened"])

        time.sleep(10)
        GPIO.output(locketPin, False)
        sio.emit(socketEmits["locket_closed"])
    except:
        sio.emit(socketEmits["locket_opening_error"])
        print("Fail:")
        print("Failed to open fridge")
    finally:
        GPIO.cleanup()


@sio.event
def disconnect():
    print('disconnected from server')


# socket.io connection to server
sio.connect('ws://localhost:3002')
sio.wait()
