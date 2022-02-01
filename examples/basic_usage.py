# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *

client = Client("faryna747pavlo@gmail.com", "killer4321")


print('Own id: {}'.format(client.uid))

client.sendMessage("myr", client.uid, ThreadType.USER)


client.logout()
