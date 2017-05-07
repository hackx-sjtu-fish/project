import db.common as db
from models.message import MessageType, Message
from flask import jsonify, Flask, request
import requests
import dateutil.parser
from flask_cors import CORS
from gevent.wsgi import WSGIServer

# Fill your own backend here!
BACKEND_URL=''
app = Flask(__name__)
CORS(app)

@app.teardown_request
def shutdown_session(exception=None):
    db.db_session.remove()

def get_message():
    req = request.args
    if 'since' in req:
        since_time = req['since']
        msgs = Message.query.filter(Message.date >= dateutil.parser.parse(since_time)).order_by(Message.date)
        msgs = [x for x in map(lambda m: m.as_dict(), msgs)]
    else:
        print('query msg')
        msgs = Message.query.order_by(Message.date.desc()).limit(100)
        msgs = [x for x in map(lambda m: m.as_dict(), msgs)]
        print('result=', msgs)
        msgs = msgs[::-1]
    return jsonify(msgs)

def add_message():
    req = request.json
    msg = Message(username=req['username'], date=dateutil.parser.parse(req['date']),
                  type=MessageType.PHOTO if req['type'] == 'photo' else MessageType.TEXT)
    if msg.type == MessageType.TEXT:
        msg.text = req['text']
    else:
        msg.photo = req['photo']
        print('sending to backend with url=', msg.photo)
        r = requests.get(BACKEND_URL, json={'photo': msg.photo})
        print('backend return=', r.text)
        msg.emoji = r.json()['emoji']

    db.db_session.add(msg)
    db.db_session.commit()

    return jsonify('')



@app.route('/chat/message', methods=['GET', 'POST'])
def handle_message():
    if request.method == 'GET':
        return get_message()
    else:
        return add_message()

if __name__ == '__main__':
    db.init_db()
    http_server = WSGIServer(('', 8080), app)
    http_server.serve_forever()
