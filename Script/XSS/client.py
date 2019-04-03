#!/bin/python
from selenium import webdriver
import time
options = webdriver.firefox.options.Options()
options.add_argument("--headless")
drv = webdriver.Firefox(options=options, executable_path="./geckodriver")
drv.get("http://localhost/xss.html")
drv.add_cookie({"name":"user","value":"WillieWonka"})
drv.add_cookie({"name":"passwd","value":"Il0v3C4ndys!"})
while True:
	frun = open('DoNotTouch.txt','r')
    run = frun.read()
    if run == '1':
    	drv.get("http://localhost/xss.html")
   		time.sleep(10)
