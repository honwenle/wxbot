# coding: utf-8
from wxpy import *
import os
import random

bot = Bot(cache_path = True)
noclip = bot.friends().search('微杏')[0]
fuli = bot.groups().search('福利')[0]
@bot.register([noclip,fuli], TEXT)
def recive_group_message(msg):
    print(msg.chat.name + ': ' + msg.text)
    if msg.text == '福利':
        try:
            os.chdir('./mzitu')
            dirlist = os.listdir();
            adir = dirlist[int(random.random() * len(dirlist))]
            os.chdir(adir)
            imglist = os.listdir();
            aimg = imglist[int(random.random() * len(imglist))]
            print(aimg)
            msg.reply_image(aimg)
            os.chdir('../../')
        except Exception:
            print(Exception.message)
embed()