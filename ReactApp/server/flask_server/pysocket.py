import threading

from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def set_interval(func, event, link, sec):
    print("Set Interval Running")
    def func_wrapper():
        set_interval(func, event, link, sec)
        func(event, link)
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

@socketio.on('connection')
def handle_my_custom_event():
    set_interval(emit, 'FromAPI', 'https://www.youtube.com/watch?v=_V3StKhHTyw', 10)

if __name__ == '__main__':
    socketio.run(app)
