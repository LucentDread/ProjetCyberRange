#!/usr/bin/python

import os
from ftplib import FTP
import time

def Diff(listing, local_list):
    li_dif = [i for i in listing + local_list if i not in listing or i not in local_list]
    return li_dif

while True:
    try:
        ftp = FTP("localhost", "theo", "toort")
        print("Welcome: " + ftp.getwelcome())
        ftp.login("theo","toort")
        listing = []
        ftp.cwd("Images")
        ftp.retrlines('LIST', listing.append)
        filenames = [x[-1].lstrip() for x in [x.split(None, 8) for x in listing]]
        local_list = os.listdir("/home/theo/Images2")
        liste_diff = Diff(filenames, local_list)
        print(liste_diff)
        for i in liste_diff:
            local_filename = os.path.join("/home/theo/Images2", i)
            lf = open(local_filename, "wb")
            ftp.retrbinary("RETR " + i, lf.write, 8*1024)
            lf.close()
        ftp.quit()

    except:
        pass
    time.sleep(5)
