import pyautogui
import time
import random
import keyboard
import smtplib, ssl

smtp_sever = 'smtp.gmail.com'
port = 587
sender_email = '<gmail email>'
receiver_email = '<recipient emailßß>'
password = input('Please enter gmail password and press enter:')

# Create a secure SSL context
#https://realpython.com/python-send-email/#sending-a-plain-text-email
context = ssl.create_default_context()
server = smtplib.SMTP(smtp_sever, port)
server.ehlo()
server.starttls(context=context) # Secure the connection
server.ehlo()
server.login(sender_email, password)
message = """Subject: Moving the mouse'
This message shows the mouse moving at:/n
"""

while(True):
    x = random.randint(0,500)
    y = random.randint(0,500)
    print('[INFO] action. About to move the mouse...')
    pyautogui.moveTo(x,y)
    output_string = 'Cursor moved to x:' + str(x) + 'y:' + str(y)
    message = message + output_string
    print(output_string)
    server.sendmail(sender_email, receiver_email, message)
    time.sleep(20)

  
    