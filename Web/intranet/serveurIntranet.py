#!/usr/bin/python
import datetime
from http.server import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep, path, system

PORT_NUMBER = 80

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
        #Log file
		f = open('/root/intranet/logs.txt','a')
		f.write("["+ str(datetime.datetime.now()) + "]" + self.path + "requested by " + self.address_string() + "\n")
        
        #basic path
		if self.path=="/":
			self.path="/index.html"
        
        #Check for a value : path to a file
		p = self.path
		if '?' in p:
			path2, args = p.split('?')
			if args :
				var, path2 = args.split('=')
				if path2 :
					self.path = path2

		try:
            #if the path is a directory
            if(os.path.isdir(self.path)):
                self.send_response(200)
                self.send_header('Content-type','text/plain')
                self.end_headers()
                items = os.listdir()
                text = ''
                for i in items:
                    text = text + i + '\n'
                self.wfile.write(text)
                
            #if the path is a file
            elif(os.path.isfile(self.path)):
			#Check the file extension required and
			#set the right mime type

                sendReply = False
                if self.path.endswith(".txt"):
                    mimetype='text/plain'
                    sendReply = True
                if self.path.endswith(".html"):
                    mimetype='text/html'
                    sendReply = True
                if self.path.endswith(".jpg"):
                    mimetype='image/jpg'
                    sendReply = True
                if self.path.endswith(".png"):
                    mimetype='image/png'
                    sendReply = True
                if self.path.endswith(".gif"):
                    mimetype='image/gif'
                    sendReply = True
                if self.path.endswith(".pdf"):
                    mimetype='application/pdf'
                    sendReply = True
                if self.path.endswith(".js"):
                    mimetype='application/javascript'
                    sendReply = True
                if self.path.endswith(".css"):
                    mimetype='text/css'
                    sendReply = True

                if sendReply == True:
                    #Open the static file requested and send it
                    if path.exists("root/intranet" + self.path) :
                        f = open("root/intranet" + self.path, 'rb')
                        self.send_response(200)
                        self.send_header('Content-type',mimetype)
                        self.end_headers()
                        self.wfile.write(f.read())
                        f.close()
                    else:
                        self.send_error(404,'File Not Found: %s' % self.path)
                else:
                    self.send_error(404,'File Not Found: %s' % self.path)
                return

            else: 
                self.send_error(404,'File Not Found: %s' % self.path)
                
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print('Started httpserver on port ' , PORT_NUMBER)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print('^C received, shutting down the web server')
	server.socket.close()
