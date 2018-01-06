# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return 'hello Flask'
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

# from myapp import acount
#
# acount.account()


import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(2)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()