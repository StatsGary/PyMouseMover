""" 
Name:       MouseJiggleAP.py
Author:     Gary Hutson
Date:       12/01/2022
Purpose:    Jiggling mouse when inactive to appear active on Slack and MS Teams
            Helps when working across two machines and not being monitored

Usage:      python MouseJiggleAP.py --wait 5
            (Command to run in terminal, prompt or PS window)
            Waits for 5 seconds before looping through next mouse location

            python MouseJiggleAP.py --wait 10
"""

import pyautogui
import time
import random
import os
import getpass
import argparse as ap


USERNAME = getpass.getuser()
#Create argument parser to sort out the wait time\

# Create argument parser to define wait time
parser = ap.ArgumentParser()
parser.add_argument('-w', '--wait', required=True, 
        help='Wait time for mouse mover')
args = vars(parser.parse_args())

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
        print('\nCTRL + C pressed and keyboard interupt terminated by {}!'.format(USERNAME))
        break


  
    