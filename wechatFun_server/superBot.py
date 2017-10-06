from wxpy import Bot
import threading
import uuid

class SuperBotTread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadID = uuid.uuid4().hex

    def run(self):
        "Starting " + self.name
        self.bot = Bot(qr_path = 'static/'+self.threadID+'.png')
        return



    def bot_login_qr_callback(self):
        pass



class BotPool(object):
    def __init__(self):
        #self.
        pass