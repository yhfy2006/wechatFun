
from .msgModule import *

class MsgAutoReply(MsgModule):

    msgType = "Text"

    def __init__(self,puid):
        super().__init__(puid)
        self.moduleId = MsgModuleCode.Msg_Auto_Reply

    def execute(self,msg):

        preDefinedMessage = "this is a predefined knowledge"
        msg.reply(preDefinedMessage)


