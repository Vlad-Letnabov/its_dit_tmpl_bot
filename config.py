# -*- coding: utf-8 -*-
import telebot
import xml.etree.ElementTree as ET

class Config():

    def __init__(self):
        print('init config')
        config = dict()

    def get_config(self):
        tree = ET.parse('config.xml')
        root = tree.getroot()
        # все данные
        print('Expertise Data:')
        result = dict()

        for elem in root:
            # print(elem.tag + ' - ' + str(len(list(elem))) )
            # print(type(elem))
            if (len(list(elem)) > 0):
                result[elem.tag] = dict()
                for subelem in elem:
                    result[elem.tag][subelem.tag] = subelem.text
            else:
                result[elem.tag] = elem.text
        return result
