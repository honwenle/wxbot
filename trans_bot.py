# coding: utf-8
from wxpy import *
import re
from trans_baidu import trans

bot = Bot(cache_path = True)
d = bot.groups().search('亲爱的')[0]
lls4993 = bot.groups().search('4993班')[0]
fuli = bot.groups().search('福利')[0]
@bot.register([Friend, lls4993, fuli], TEXT)
def recive_group_message(msg):
    print(msg.chat.name + ': ' + msg.text)
    r = re.compile(r'^[a-zA-Z]')
    result = r.match(msg.text)
    if result != None:
        transre = trans(msg.text)
        if len(transre['trans_result']) > 0:
            transre = transre['trans_result'][0]['dst']
            msg.reply(transre)
embed()