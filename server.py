from flask import Flask
from flask import request
from tinydb import TinyDB
import time
import json
app = Flask(__name__)

db = TinyDB('scores.ldb')

@app.route('/scores', methods=['POST', 'GET'])
def scores():
    if request.method == 'GET':
        return json.dumps({'success': True, 'data': db.all()})
    elif request.method == 'POST':
        # self.db.insert({'score' : self.score, 'level': self.level, 'time': time.time() - self.start_time})
        db.insert({'score': int(request.form['score']), 'level': int(request.form['level']), 'time': float(request.form['time']), 'name': request.form['name']})
        return json.dumps({'success': True})

@app.route('/scores/highest')
def get_high_score():
    highest_item = None
    for item in iter(db):
        if highest_item is None:
            highest_item = item
        else:
            if highest_item['score'] < item['score']:
                highest_item = item
    return json.dumps({'success': True, 'data': highest_item})

@app.route('/handshake')
def handshake():
    return 'Hello From Tetris Scoreboard server%&%' + str(time.time()) + '%&%Hello, World!'