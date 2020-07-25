import telebot
import xml.etree.ElementTree as ET
import sys
import logging

#x = ET.fromstring(data)
FORMAT = '%(asctime)s %(name)s %(levelname)s %(message)s'
# logging.basicConfig(format=FORMAT)
LOG_LEVEL = 'INFO'
LOG_FILE = 'logs/sample.log'
def get_config():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    # все данные
    print('Expertise Data:')
    result = dict()

    for elem in root:
        #print(elem.tag + ' - ' + str(len(list(elem))) )
        #print(type(elem))
        if (len(list(elem))>0):
            result[elem.tag] = dict()
            for subelem in elem:
                result[elem.tag][subelem.tag]=subelem.text
        else:
            result[elem.tag]=elem.text
    return result

config = get_config()
if 'logging' in config:
    if 'level' in config['logging']:
        LOG_LEVEL = config['logging']['level']
    if 'file' in config['logging']:
        LOG_FILE = config['logging']['file']
print(LOG_LEVEL)
print(LOG_FILE)
print('-------------------------------------')
print(str(config))
logging.basicConfig(filename=LOG_FILE, level=LOG_LEVEL, format=FORMAT)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")
try:
    bot = telebot.TeleBot(config['token'])
except BaseException as exp:
    print('ERROR: ' + str(exp))
    sys.exit(str(exp))

bot.polling(none_stop=True, interval=0)



@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
