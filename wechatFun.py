from wxpy import *
bot = Bot()
my_friend = bot.friends()

tuling = Tuling('fb37998bdc04e7e2d2aa8c9395ecf142')

# Receive message automatically
@bot.register()
def print_others(msg):
    print(msg)


# Reply message
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)
    #return 'I just received your call, received: {} ({})'.format(msg.text, msg.type)

embed()