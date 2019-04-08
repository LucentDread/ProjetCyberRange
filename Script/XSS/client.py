#!/bin/python
from selenium import webdriver
import time

# Load Firefox options
options = webdriver.firefox.options.Options()
# With headless option
options.add_argument("--headless")
# Specify gecko driver path
drv = webdriver.Firefox(options=options, executable_path="./geckodriver")

# Load the page with the rights cookies
drv.get("http://localhost/xss.html")
drv.add_cookie({"name":"user","value":"WillieWonka"})
drv.add_cookie({"name":"passwd","value":"Il0v3C4ndys!"})

# While activated, reload the pages
while True:
	frun = open('DoNotTouch.txt','r')
    run = frun.read()
    if run == '1':
    	drv.get("http://localhost/xss.html")
   		time.sleep(10)
