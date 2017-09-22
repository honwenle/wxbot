from wxpy import *

bot = Bot(cache_path = True)
tl = Tuling(api_key='7bc905adb9b242d08a85cd55dabf9558')
fuli = bot.groups().search('福利')[0]
dear = bot.friends().search('亲爱的')[0]
til = bot.friends().search('TIL')[0]

@bot.register([Friend,fuli])
def tlbotreply(msg):
    print(msg.chat.name + ': ' + msg.text)
    tl.do_reply(msg)

@bot.register(dear)
def ignoredear(msg):
    print(msg.chat.name + ': ' + msg.text)

embed()