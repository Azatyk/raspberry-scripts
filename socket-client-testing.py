import socketio

sio = socketio.Client()


@sio.event
def connect():
    print('connection established')

# @sio.event
# def my_message(data):
#     print('message received with ', data)


@sio.event
def disconnect():
    print('disconnected from server')


sio.connect('http://localhost:3002')

sio.emit('message', "It is python client message, bitch")
sio.wait()
