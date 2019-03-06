from fbchat import Client
from fbchat.models import *
import logging
from datetime import datetime

talking_to = ['Ioana Stoian', 'Costa Anton', 'Andrei Stamate', 'Oana Blair', 'Dan Moss']
last = None


class CustomClient(Client):
    def onMessage(self, mid, author_id, message_object, thread_id, thread_type, ts, metadata, msg, **kwargs):
        global last

        if author_id != self.uid:
            for u in talking_to:
                user = client.searchForUsers(u)
                user = user[0]
                if user.uid == author_id:
                    if last != user.first_name:
                        print("\n{} {}:".format(user.first_name, user.last_name))
                    last = user.first_name
                    break
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": " + message_object.text)


user = input('Username:')
passw = input('Pass:')
client = CustomClient(user, passw, logging_level=logging.ERROR)

client.listen()

client.logout()