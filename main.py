from flask import Flask
from flask.templating import render_template
from flask_socketio import SocketIO
from sms import SMSClient

app = Flask(__name__)

socketio = SocketIO(app)

ACCESS_KEY = "iNExJakwOx2F2w37CzwWGi7aF"
ID = "5a65cea8-ee01-40c4-a841-a152d2b4d71a"


@app.route('/')
def home_page():
    ACCESS_KEY = "iNExJakwOx2F2w37CzwWGi7aF"
    ID = "5a65cea8-ee01-40c4-a841-a152d2b4d71a"
    return render_template('chat.html')


if __name__ == "__main__":
    socketio.run(app, debug=True)