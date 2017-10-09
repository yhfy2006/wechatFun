import io
from flask import Flask, send_file, request, abort
from superBot import SuperBotTread
from superBot import BotPool
import os.path

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/newbot")
def newBot():
    bot = SuperBotTread()
    bot.start()
    return bot.threadID


@app.route("/qr/<botid>")
def returnQRImg(botid):
    imgName = 'static/'+botid+'.png'
    if os.path.isfile(imgName):
        return send_file(imgName, mimetype='image/png')
    else:
        abort(404)

@app.route('/loginstatus/<botid>')
def returnLoginStatus(botid):
    bot = BotPool().shared.getBotThread(botid)
    if bot is not None:
        return str(bot.status.value)
    abort(404)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

def qr_callback(uuid, status, qrcode):
    # with open("static/qr.png", 'rb') as bites:
    #     return send_file(
    #         io.BytesIO(bites.read()),
    #         attachment_filename='logo.jpeg',
    #         mimetype='image/jpg'
    #     )
    return send_file(
            io.BytesIO(qrcode),
             attachment_filename='logo.jpeg',
             mimetype='image/jpg'
         )


if __name__ == '__main__':
    app.run()