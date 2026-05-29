import time
import redis
from flask import Flask

app = Flask(__name__)
# 注意： redis 服务器就是 docker-compose 里定义的服务名
import os
cache = redis.from_url(os.environ.get('REDIS_URL'))

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)

@app.route('/')
def hello():
    count = get_hit_count()
    return f'Hello from Docker! 你是第 {count} 位访客。\n'

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000) 
