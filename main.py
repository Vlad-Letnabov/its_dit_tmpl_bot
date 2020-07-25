import telebot
import xml.etree.ElementTree as ET

#x = ET.fromstring(data)
#bot = telebot.TeleBot('%ваш токен%')

def get_config():
    tree = ET.parse('config.xml')
    root = tree.getroot()
    # все данные
    print('Expertise Data:')
    result = dict()

    for elem in root:
        print(elem.tag + ' - ' + str(len(list(elem))) )
        #print(type(elem))
        if (len(list(elem))>0):
            print('HAS')
            result[elem.tag] = dict()
            for subelem in elem:
                print('\t' + subelem.tag + ' : ' + subelem.text) #' - '+ subelem.attrib['id'] +
                result[elem.tag][subelem.tag]=subelem.text
        else:
            print('EBSENT')
            print(elem.tag + ': ' + elem.text)
            result[elem.tag]=elem.text
    return result

config = get_config()
print('-------------------------------------')
print(str(config))



'''@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.") '''