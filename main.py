from flask import Flask
from flask.templating import render_template
from flask_socketio import SocketIO
from sms import SMSClient

app = Flask(__name__)

socketio = SocketIO(app)

@app.route('/')
def home_page():
    return render_template('chat.html')


if __name__ == "__main__":
    socketio.run(app, debug=True)