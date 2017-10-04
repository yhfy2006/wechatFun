# -*- coding: utf-8 -*-
from wxpy import *
import re
bot = Bot()
my_friend = bot.friends()

# 0 = AUTOREPLAY
# 1 = Identity
# 2 = tuling
mode = 0

tuling = Tuling('fb37998bdc04e7e2d2aa8c9395ecf142')

# Receive message automatically
@bot.register()
def print_others(msg):
    print(msg)


# Reply message
@bot.register(my_friend)
def reply_my_friend(msg):
    #tuling.do_reply(msg)
    replyMessages(msg)
    #return 'I just received your call, received: {} ({})'.format(msg.text, msg.type)




def replyMessages(msg):
    message = msg.text
    messageType = ''
    global mode
    if re.match('@\d',message) is not None:
        messageType = re.match('@\d',message).group()
    if messageType == "@1" :
        msg.reply("切换到自动回复模式:")
        mode = 0

    elif messageType == '@2':
        msg.reply("切换到身份检测模式:")
        mode = 1

    elif messageType == "@3":
        mode = 2
        msg.reply("切换到自动机器人模式 请说任意话")
        return

    if mode == 0:
        msg.reply("你好 欢迎来到我的世界，我的世界里有一个非常牛逼的自由的灵魂。这条消息是自动回复的哦")

    if mode == 1:
        sender = msg.sender
        identity = '用户名 {} \n 性别{} \n 来自{} \n 签名:{} \n'.format(sender.nick_name, sender.sex,sender.city,sender.signature)
        msg.reply(identity)

    if mode == 2:
        tuling.do_reply(msg)


embed()