import io
import os.path

from flask import Flask, send_file, abort

from blueprints.user import user
from blueprints.bot import botPrint

import leancloud

from cloud import engine

APP_ID = '3WWukkAWiSBeNUyqbishuYxS-gzGzoHsz'
APP_KEY = 'JWtVecWMHtu9E0rNo7RBbVsg'
MASTER_KEY ='9B6R2qAlKqKnzXy4imF0Gc8p'
PORT = 5000

leancloud.init(APP_ID, app_key=APP_KEY, master_key=MASTER_KEY)
# 如果需要使用 master key 权限访问 LeanCLoud 服务，请将这里设置为 True
leancloud.use_master_key(False)


app = Flask(__name__)

#注册蓝图
app.register_blueprint(botPrint)
app.register_blueprint(user)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()