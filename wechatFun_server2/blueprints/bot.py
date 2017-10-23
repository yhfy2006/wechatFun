import sys
sys.path.append("../")
from flask import Blueprint,abort,send_file
from components.superBot import SuperBotTread,BotPool
import os

botPrint = Blueprint('bot',__name__)


@botPrint.route("/bot/newbot")
def newBot():
    bot = SuperBotTread()
    bot.start()
    return bot.threadID


@botPrint.route("/bot/qr/<botid>")
def returnQRImg(botid):
    imgName = 'static/'+botid+'.png'
    if os.path.isfile(imgName):
        return send_file(imgName, mimetype='image/png')
    else:
        abort(404)

@botPrint.route('/bot/loginstatus/<botid>')
def returnLoginStatus(botid):
    bot = BotPool().shared.getBotThread(botid)
    if bot is not None:
        return str(bot.status.value)
    abort(404)


@botPrint.route('/bot/chat/autoReply/<botid>')
def setAutoReplyMessage(botid):
    bot = BotPool().shared.getBotThread(botid)
    if bot is not None:
        return str(bot.status.value)
    abort(404)
