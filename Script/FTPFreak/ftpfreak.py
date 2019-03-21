!/usr/bin/python

import os
from ftplib import FTP
import time

def Diff(listing, local_list):
    li_dif = [i for i in listing + local_list if i not in listing or i not in local_list]
    return li_dif


while True:
    try:
        ftp = FTP("fdp.com", "USERNAME", "PASSWORD")
        print "Welcome: ", ftp.getwelcome()
        ftp.login()

        # listing des fichiers
        ftp.retrlines("LIST")

        ftp.cwd("folderOne")
        ftp.cwd("subFolder")

        listing = []
        ftp.retrlines('LIST', listing.append)
        words = listing[0].split(None, 8)
        filename = words[-1].lstrip()

        local_list = []
        local_list = os.listdir('c:/python24')

        liste_diff = Diff(listing, local_list)

        # téléchargement fichier
        for i in liste_diff:
            local_filename = os.path.join(r"c:\myfolder", i)
            lf = open(local_filename, "wb")
            ftp.retrbinary("RETR " + i, lf.write, 8*1024)
            lf.close()

        connection().quit()
        time.sleep(30)
