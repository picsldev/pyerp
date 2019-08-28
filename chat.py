#!/usr/bin/env python3
import eventlet
import socketio

sio = socketio.Server(cors_allowed_origins='*')
app = socketio.WSGIApp(sio)


@sio.event
def connect(sid, environ):
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.on('chat')
def message_chat(sid, message):
    print(message)
    print('chat-%s' % sid)
    sio.emit('chat-%s' % sid, 'Hemos recibido su pregunta: %s' % message)


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)
