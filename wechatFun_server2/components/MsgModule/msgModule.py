
import enum
from abc import abstractmethod

class MsgModuleCode(enum.Enum):
    Msg_none = -1
    Msg_Auto_Reply = 0

class MsgModule(object):

    def __init__(self,puid):
        self.bot_puid = puid
        self.moduleId = MsgModuleCode.Msg_none

    @abstractmethod
    def execute(self):
        pass








