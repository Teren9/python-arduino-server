import serial
import SimpleHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
from time import sleep
from urlparse import parse_qs
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

ser = serial.Serial('/dev/ttyACM0', 9600)

def write_from_user(foo):
	ser.write(foo)

def read_from_serial():
   # sleep(0.05)
    return ser.readline()

SocketServer.TCPServer.allow_reuse_address = True

PORT = 5050

class myHandler(SimpleHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		if (self.path == "/"):
			SimpleHTTPRequestHandler.do_GET(self)
			return
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		# Send the html message
		operation = self.path[1:][0]
		write_from_user(operation)
		write_from_user(chr(int(self.path[2:])))
		if (operation == 'R'):
			response = "{"+'"Response":"{0}"'.format(read_from_serial()[:-2])+"}"
			self.wfile.write(response)
		return


#Handler = SimpleHTTPRequestHandler

Handler = myHandler
try:
	httpd = SocketServer.TCPServer(("", PORT), Handler)

	print "serving at port", PORT
	httpd.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	httpd.socket.close()

