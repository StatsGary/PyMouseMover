""" 
Name:       MouseJiggle.py
Author:     Gary Hutson
Date:       12/01/2022
Purpose:    Jiggling mouse when inactive to appear active on Slack and MS Teams
            Helps when working across two machines and not being monitored
"""

import pyautogui
import time
import random
import os
import getpass
import argparse as ap


USERNAME = getpass.getuser()
#Create argument parser to sort out the wait time
parser = ap.ArgumentParser()
parser.add_argument('-w', '--wait', required=True, help='Wait time for mouse mover')
args = vars(ap.parse_args())

WAIT_TIME = int(args['wait'])

while(True):
    try:
        x = random.randint(0,500)
        y = random.randint(0,500)
        print('-' * 80)
        print('[INFO] action triggered by {}. About to move the mouse... '.format(USERNAME))
        pyautogui.moveTo(x,y)
        output_string = 'Cursor moved to x: ' + str(x) + 'y: ' + str(y)
        print(output_string)
        print('[INFO Cursor has been moved.]')
        print('-' * 80)
        time.sleep(WAIT_TIME)
    except KeyboardInterrupt:
        print('CTRL + C pressed and keyboard interupt terminated by {}!'.format(USERNAME))
        break


  
    