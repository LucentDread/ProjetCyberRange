import easyimap
import pickle
from email.header import decode_header
import os
import time

#Creds for the email account, if needed
login = ''
password = ''

seenMails = []

while True:
    #check the flag file to check the emails or not
    frun = open('DoNotTouch.txt','r')
    run = frun.read()
    if run == '1':
        #retrieve mails already seen from the picke
        if os.stat("seenMails.txt").st_size != 0 :
            with open ('seenMails.txt', 'rb') as fp:
                seenMails = pickle.load(fp)

        imapper = easyimap.connect('outlook.office365.com', login, password)

        #retrieve the 3 last mails
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
                    #for each attachement in every mail : load then execute
                    for attachment in mail.attachments:
                        if '?iso-8859-1?' in attachment[0]:
                            temp = decode_header(attachment[0])[0]
                            f = open("attachments/" + temp[0].decode('utf-8'), "wb")
                            f.write(attachment[1])
                            f.close()
                            toExec.append(temp[0])
                        else:
                            f = open("attachments/" + attachment[0], "wb")
                            f.write(attachment[1])
                            f.close()
                            toExec.append(attachment[0])
                    for f in toExec:
                        print(f)
                        os.system('explorer.exe "attachments\\'+f+'"')
                except Exception as e:
                    print(str(e))
                    pass

        #put every seen mails into the pickle file
        with open('seenMails.txt', 'wb') as fp:
            pickle.dump(seenMails, fp)

        print('waiting next iteration ------')
        time.sleep(120)
    frun.close()