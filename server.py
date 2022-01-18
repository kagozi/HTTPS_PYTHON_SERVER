import http.server
import socket
import ssl
import os


server_address = ('0.0.0.0', 9000)
#returns the host name of the current system under which the Python interpreter is executed:
hostname = socket.gethostname()   
# Get the IP address of the local host:
local_ip = socket.gethostbyname(hostname) 
 
print("Open https://localhost:9000")
print('Open https://' + local_ip + ':9000')


#os.chdir("./dist/")

class CORSHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    #maps dictionaries into MIME types i.e text, html, .ico, .ics..etc
    extensions_map = {                            
        '': 'application/octet-stream',
        '.manifest': 'text/cache-manifest',
        '.html': 'text/html',
        '.png': 'image/png',
        '.jpg': 'image/jpg',
        '.svg':	'image/svg+xml',
        '.css':	'text/css',
        '.js': 'application/x-javascript',
        '.wasm': 'application/wasm',
        '.json': 'application/json',
        '.xml': 'application/xml',
    }

    def end_headers(self):
        # Include additional response headers here. CORS for example:
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        http.server.SimpleHTTPRequestHandler.end_headers(self)

    
#This class builds on the TCPServer class by storing the server address as instance variables named server_name and server_port:
httpd = http.server.HTTPServer(server_address, CORSHTTPRequestHandler) 
#the ssl.SSLContext class helps manage settings and certificates:
#ssl.PROTOCOL_TLS_SERVER: Auto-negotiate the highest protocol version that both the client and server support:
ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
#Perform the SSL setup handshake:
ctx.check_hostname = False
# Load a private key and the corresponding certificate:
ctx.load_cert_chain(certfile='C:\\Users\\ALEX\\Desktop\\secureserver\\cert.pem')  # with key inside
#returns a new context with secure default settings:
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
#Handle requests until an explicit shutdown() request:
httpd.serve_forever()