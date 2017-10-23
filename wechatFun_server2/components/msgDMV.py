from .MsgModule.msgModule import *
from .MsgModule.msgAutoReply import *


class MessageDMV(object):
    def __init__(self,puid):
        self.bot_puid = puid

        # Key:msg_type    Value:msgModule_instance
        self.serviceProcessDict = {}

        self._classModuleMap = None
        self.registerServices()

    @property
    def classModuleMap(self):
        dict ={
            MsgModuleCode.Msg_Auto_Reply : MsgAutoReply
        }
        return dict

    def registerServices(self):
        services = self.checkSubscribedServices()
        for s in services:
            newServiceClass = self.classModuleMap[s]
            newService = newServiceClass(self.bot_puid)
            if newService.msgType in self.serviceProcessDict:
                typeServiceArray = self.serviceProcessDict[s.msgType]
                typeServiceArray.append(newService)
            else:
                typeServiceArray =[newService]

            self.serviceProcessDict[newService.msgType] = typeServiceArray

    def checkSubscribedServices(self):
        #read from DB
        return [MsgModuleCode.Msg_Auto_Reply]


    def processMessage(self,msg):

        #以后用多线程？
        if msg.type in self.serviceProcessDict:
            for service in self.serviceProcessDict[msg.type]:
                service.execute(msg)


if __name__ == '__main__':
    pass
