import io
import os.path

from flask import Flask, send_file, abort

from blueprints.user import user
from blueprints.bot import botPrint

app = Flask(__name__)

#注册蓝图
app.register_blueprint(botPrint)
app.register_blueprint(user)


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run()