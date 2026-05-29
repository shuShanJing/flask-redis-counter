import os
import redis
from flask import Flask, render_template

app = Flask(__name__)
redis_url = os.environ.get('REDIS_URL', 'redis://redis:6379')
cache = redis.from_url(redis_url)

@app.route('/')
def home():
    count = cache.incr('hits')
    return render_template('index.html', count=count)

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/fun')
def fun():
    return render_template('fun.html')

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000) 
