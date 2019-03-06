from fbchat import Client
from fbchat.models import *
import logging

user = input('Username:')
passw = input('Pass:')
client = Client(user, passw, logging_level=logging.ERROR)
while 1:
    msg = input()
    user, msg = msg.split('$')
    user = client.searchForUsers(user)
    client.send(Message(text=msg), thread_id=user[0].uid, thread_type=ThreadType.USER)
