from wxpy import Bot
import threading
import uuid
import enum
import base64


class BotStatus(enum.Enum):
    login_none = 0
    login_qr_waiting = 1
    login_success = 2
    login_fail = 3



class SuperBotTread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.threadID = uuid.uuid4().hex
        self.status = BotStatus.login_none
        BotPool().shared.addBotThread(self.threadID,self)

    def run(self):
        print("Starting " + self.name)
        self.bot = Bot(qr_path = 'static/'+self.threadID+'.png',
                       login_callback=self.bot_login_callback ,
                       qr_callback= self.bot_login_qr_callback,
                       logout_callback= self.bot_logout_callback )
        return



    def bot_login_qr_callback(self,uuid, status, qrcode):
        print("QR sent " + self.threadID)
        self.status = BotStatus.login_qr_waiting
        filename = 'static/'+self.threadID+'.png'
        with open(filename, 'wb') as f:
            f.write(qrcode)


    def bot_login_callback(self):
        print("Login_success " + self.threadID)
        self.status = BotStatus.login_success


    def bot_logout_callback(self):
        print("Logout_success " + self.threadID)
        self.status = BotStatus.login_none


    @Bot.register()
    def register_events(self,msg):
        if msg.type == 'Friends':
            print(msg)







class BotPool(object):
    shared = None
    __botPoolDict = {}
    def __new__(cls):
        if BotPool.shared is None:
            BotPool.shared = object.__new__(cls)
        return BotPool.shared

    def addBotThread(self,key,bot):
        self.__botPoolDict[key] = bot

    def getBotThread(self,key):
        return self.__botPoolDict.get(key)

if __name__ == '__main__':
    print(BotPool().shared)
    print(BotPool().shared)