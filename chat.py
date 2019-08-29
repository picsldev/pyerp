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
    sio.emit('master', {
        'sid': sid,
        'message': message
    })


@sio.on('chatr')
def message_response(sid, data):
    sio.emit('chat-%s' % data['sid'], data['message'])


if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
