import easyimap
import pickle
from email.header import decode_header
import os
import time

login = ''
password = ''

seenMails = []

while True:
    if os.stat("seenMails.txt").st_size != 0 :
        with open ('seenMails.txt', 'rb') as fp:
            seenMails = pickle.load(fp)

    imapper = easyimap.connect('outlook.office365.com', login, password)

    for mail_id in imapper.listids(limit=3):
        mail = imapper.mail(mail_id)
        if (mail.title, mail.date) not in seenMails:
            seenMails.append((mail.title, mail.date))
            print(mail.from_addr)
            print()
            print(mail.to)
            print()
            print(mail.title)
            print()
            
            toExec = []
            try:
                for attachment in mail.attachments:
                    if '?iso-8859-1?' in attachment[0]:
                        temp = decode_header(attachment[0])[0]
                        f = open("attachments/" + temp[0].decode('utf-8'), "wb")
                        f.write(attachment[1])
                        f.close()
                        toExec.append(temp[0])
                        print(temp[0])
                    else:
                        f = open("attachments/" + attachment[0], "wb")
                        f.write(attachment[1])
                        f.close()
                        toExec.append(attachment[0])
                        print(attachment[0])
                #TODO : open les trucs
                for f in toExec:
                    print(f)
                    os.system('explorer.exe "attachments\\'+f+'"')
            except Exception as e:
                print(str(e))
                pass
    
    with open('seenMails.txt', 'wb') as fp:
        pickle.dump(seenMails, fp)
                
    print('waiting next iteration ------')
    time.sleep(120)
