from flask import Flask, render_template
from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
socketio = SocketIO(app)


@app.route('/')
def sessions():
    return render_template('chat.html')


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('messageSent')
def handle_messageSent(json, methods=['GET', 'POST']):
    print('Message Sent: ' + str(json))
    socketio.emit('message', json, callback=messageReceived)


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


if __name__ == '__main__':
    socketio.run(app)