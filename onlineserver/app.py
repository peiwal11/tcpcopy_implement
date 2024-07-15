from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import sys
data = {'result': 'this is a test'}

class Request(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
       # self.wfile.write(json.dumps(data).encode())
        self.wfile.write(f"welcome from {self.server.server_port} \n".encode('utf-8'))
        print(f"port: {self.server.server_port} response")
def run():
    server_class = HTTPServer
    handler_class=Request
    port = int(sys.argv[1]) if len(sys.argv)>1 else  9999
    server_address=('',port)
    print(f"response from: {server_address[0]}:{server_address[1]}\n")
    httpd = server_class(server_address,handler_class)

    httpd.serve_forever()
if __name__ == '__main__':
    run()
