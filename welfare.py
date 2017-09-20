# coding: utf-8
from wxpy import *
import os
import random

bot = Bot(cache_path = True)
noclip = bot.friends().search('微杏')[0]
fuli = bot.groups().search('福利')[0]
@bot.register()
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
@bot.register(msg_types=PICTURE)
def recive_pic_message(msg):
    print(msg)
    msg.get_file('pics/'+msg.file_name)
embed()