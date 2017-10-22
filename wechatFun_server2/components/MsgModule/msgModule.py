
import enum
from abc import abstractmethod
class MsgDMVModule(enum.Enum):
    Msg_Auto_Reply = 0

class MsgModule(object):

    def __init__(self,puid,msg):
        self.bot_puid = puid
        self.msg = msg

    @abstractmethod
    def execute(self):
        pass








