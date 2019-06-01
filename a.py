import vk_api.vk_api
import vk_api.longpoll as vkl
import vk_api.bot_longpoll as vkb
import time


def write(uid, msg):
        vk.method('messages.send', {'peer_id': uid,
                                    'random_id': round(time.time() * 100000),
                                    'message': msg})


vk = vk_api.VkApi(token='')
longpoll = vkb.VkBotLongPoll(vk, 182022767)
chat_ids = [57, 82]
ccp = 2000000000

for event in longpoll.listen():
    if event.type == vkb.VkBotEventType.MESSAGE_NEW:
        if event.obj.peer_id != event.obj.from_id:
            print(event.obj)
            if event.obj['text'] == '1':
                write(event.obj['peer_id'], 'hello, chat')
            print('-' * 30)
        if event.obj.peer_id == event.obj.from_id:
            print(event.obj)
            if event.obj['text'] == '1':
                write(event.obj['peer_id'], 'hello, user')
            """ for key, value in event.obj.items():
                print(str(key) + " : " + str(value)) """
            print('-' * 30)
