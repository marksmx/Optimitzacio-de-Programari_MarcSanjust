#!/usr/bin/python
from http.server import HTTPServer, BaseHTTPRequestHandler
import smtplib
sender = 'marcsanjustmartinez@gmail.com'
receivers = ['marcsanjustmartinez@gmail.com']

message = """Dab
"""

class Server(BaseHTTPRequestHandler):


    def do_GET(self):
        if self.path.endswith(".jpg"):
            f = open(self.path[1:], 'rb')
            self.send_response(200)
            self.send_header('Content-type', 'image/png')
            self.end_headers()
            self.wfile.write(f.read())
            f.close()
            return

        try:
            print ("s")
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
            smtpObj = smtplib.SMTP('localhost')
            smtpObj.sendmail(sender, receivers, message)
            print ("Successfully sent email")
        except:
            file_to_open = "HTTP/1.1 404 Not Found"
            self.send_error(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open,'utf-8'))

httpd = HTTPServer(('localhost', 8080), Server)
httpd.serve_forever()
