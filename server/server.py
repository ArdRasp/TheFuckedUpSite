#!/usr/bin/env python
import http.server
 
PORT = 8888
server_address = ("", PORT)

path = "/"
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = [path]
print("Serveur actif sur le port :", PORT)

httpd = server(server_address, handler)
httpd.serve_forever()
