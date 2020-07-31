# -*- coding: utf-8 -*-
import requests


class bot():
    def __init__(self, token='12345:qwertyuiop', offset=0, limit=0, timeout=0):
        self.TOKEN = token
        self.URL = 'https://api.telegram.org/bot'

        self.offset = offset
        self.limit  = limit
        self.timeout= timeout
        self.data = dict(offset=self.offset, limit=limit, timeout=timeout)

        '''
        offset = 0 # параметр необходим для подтверждения обновления
        URL = 'https://api.telegram.org/bot' # URL на который отправляется запрос
        TOKEN = 'token' # токен вашего бота, полученный от @BotFather
        data = {'offset': offset, 'limit': 0, 'timeout': 0}
        '''

    def check_updates(self):
        for update in request.json()['result']:
            offset = update['update_id']  # подтверждаем текущее обновление

            if 'message' not in update or 'text' not in update['message']:  # это просто текст или какая-нибудь картиночка?
                print('Unknown message')
                continue

            message_data = {                                                # формируем информацию для отправки сообщения
                'chat_id': update['message']['chat']['id'],                 # куда отправляем сообщение
                'text': "I'm <b>bot</b>",                                   # само сообщение для отправки
                'reply_to_message_id': update['message']['message_id'],     # если параметр указан, то бот отправит сообщение в reply
                'parse_mode': 'HTML'                                        # про форматирование текста ниже
            }

            try:
                request = requests.post(self.URL + self.TOKEN + '/sendMessage', data=message_data)  # запрос на отправку сообщения
            except:
                print('Send message error')
                return False

            if not request.status_code == 200:  # проверим статус пришедшего ответа
                return False
        return

