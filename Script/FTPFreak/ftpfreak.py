#!/usr/bin/python

import os
from ftplib import FTP
import time

# list comparison function
def Diff(listing, local_list):
	li_dif = [i for i in listing + local_list if i not in listing or i not in local_list]
	return li_dif

	while True:
		frun = open('DoNotTouch.txt','r')
		run = frun.read()
		if run == '1':
			try:
				# FTP server connection
				ftp = FTP("localhost", "theo", "toort")
				print("Welcome: " + ftp.getwelcome())
				ftp.login("theo","toort")
				# Create a list of all the files on the ftp server
				listing = []
				ftp.cwd("Images")
				ftp.retrlines('LIST', listing.append)
				filenames = [x[-1].lstrip() for x in [x.split(None, 8) for x in listing]]
				# Create a list of all the files on the machine
				local_list = os.listdir("/home/theo/Images2")
				liste_diff = Diff(filenames, local_list)
				print(liste_diff)
				# Download files that are on the FTP server and not on the machine and save them on the machine
				for i in liste_diff:
					local_filename = os.path.join("/home/theo/Images2", i)
					lf = open(local_filename, "wb")
					ftp.retrbinary("RETR " + i, lf.write, 8*1024)
					lf.close()
					# open all new downloaded files
					os.system('explorer.exe "c:\\myfolder\\'+local_filename+'"')
					ftp.quit()

				except:
					pass
					time.sleep(5)
