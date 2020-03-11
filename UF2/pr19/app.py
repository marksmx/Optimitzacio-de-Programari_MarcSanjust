from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            #self.path="/home/msanjust/Escriptori/test/UF2/pr19/practica.html"
            self.path="bn.jpg"
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "HTTP/1.1 404 Not Found"
            self.send_error(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open,'utf-8'))

httpd = HTTPServer(('localhost', 8080), Server)
httpd.serve_forever()
