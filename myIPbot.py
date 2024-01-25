from requests import get
from sys import exit
import os
import telegram

cmd = 'dig +short txt ch whoami.cloudflare @1.0.0.1'
ip = os.popen(cmd).read()
ip = str(ip).replace('"','')

f = open('/home/pi/TelegramIPbot/ip.txt','r+') #replace path
oldIP = f.read()

if ip == oldIP:
    f.close()

else:
    f.seek(0)
    f.write(ip)
    f.truncate()
    bot = telegram.Bot("TOKEN")
    msg = 'The new IP is: ' + ip
    bot.send_message(text = msg, chat_id=ID_NUMBER)
    f.close()

exit(0)


