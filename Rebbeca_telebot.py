#!/usr/bin/python3

import time
import logging
import bs4
import requests
import argparse
import sys
import os
import config as cfg
import telepot
from telepot.loop import MessageLoop


# TODO if debug mode is enable, then log all to the file using this class
# need making sys.stdout function to the instance of Output like this 'sys.stdout = OutPut()'
class Output(object):
    '''if you set the debug mode is enable, then the program's all actions that using sys.stdout is logged to file'''

    def write(self, s):
        '''when you write something to stdout, it'll be written the file as well.'''

        open(cfg.DEBUG._FILE, 'a+').write(s)
        sys.__stdout__.write(s)


# TODO logging class
class LogAll(object):
    '''logging all important message at the file and stdout at the same time'''

    _LOGFILE = cfg.LOG4._LOGFILE
    _MAXBYTES = cfg.LOG4._MAXBYTES
    _ROTATE_CNT = cfg.LOG4._ROTATE_CNT

    
    def __init__(self):
        self.logger = logging.getLogger(LogAll._LOGFILE)
        self.logger.setLevel(logging.INFO)

        # setting up logger handlers for file and stdout
        _fhandler = logging.handlers.RotatingFileHandler(LogALL._LOGFILE, maxBytes=LogALL._MAXBYTES, backupCount=LogALL._BACKUP_CNT)
        _shandler = logging.StreamHandler()

        # add handler to logger object
        self.logger.addHandler(_fhandler)
        self.logger.addHandler(_shandler)


# TODO making cursor for sqlite3 and if it doesn't have database and tables and make them.
class ConSQL(object):
    '''Check database and supports create, delete and update field to database'''

    import sqlite3
    _DBNAME = cfg.DB4._DBNAME


    def __init__(self):
        '''if the db file exists then making cursor, if that is not created then make new db file and initialize db schema'''
        pass
        
        

class GetLotto(object):
# TODO getting last week's lotto numbers and send messages to me
    pass


class Rebbeca(telepot.Bot):
    '''This is the main class of Rebbeca, telebot!!'''

    token = cfg.INFOS._TOKEN
    admin_id = cfg.INFOS._ADMIN_ID
    public_room = cfg.INFOS._PUB_ROOMS


    def __init__(self):
        '''it tries to initiate instance of Rebbeca'''

        super(Rebbeca, self).__init__(Rebbeca.token)
        self._answerer = telepot.helper.Answerer(self)


    def check_user(self):
        '''it checks user is in admin group and then return True or False'''

        if self.from_id in Rebbeca.admin_id.keys():
            return True

        else:
            return False


    def handle(self, msg):
        '''it handles telebot message'''

        self.content_type, self.chat_type, self.chat_id = telepot.glance(msg)

        self.from_id = msg['from']['id']
        self.chat_id = msg['chat']['id']

        print(self.content_type, self.chat_type, self.chat_id, self.from_id, msg['text'])

        # TODO
        if not self.check_user():
            self.sendMessage(self.chat_id, '당신은.. 뭔데 나한테 명령이죠?')

        elif self.check_user() and self.content_type == 'text':
            self.text_msg = msg['text']

            if self.text_msg.startswith('/'):
                self.sendMessage(self.chat_id, '지금은.. 좀 바뻐요..')
                #_response = self.parsing_cmd()


## main
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Rebbeca bot Program using telepot!!')
    parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()

    if args.verbose:
        sys.stdout = Output()

    bot = Rebbeca()
    MessageLoop(bot, bot.handle).run_as_thread()

    print ('Listening ...')

# Keep the program running.

    while True:
        time.sleep(10)

