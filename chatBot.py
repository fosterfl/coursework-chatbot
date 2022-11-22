import os
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver
from urllib.parse import urlparse
import requests
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

PORT = 8080

Handler = http.server.SimpleHTTPRequestHandler
liste = []

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    global liste
    def do_GET(self):
        global liste
        parsedPath = urlparse(self.path)
        query = parsedPath.query
        self.send_response(200)

        ## V2 Mini Chatbot
        ## opens chat.html
        if parsedPath[2] != '/chat':
            root = os.path.dirname(os.path.abspath(__file__))
            filename = root + '/chat.html'
            if self.path != '/':
                filename = root + self.path

            self.send_response(200)

            if filename[-4:] == '.css':
                self.send_header('Content-type', 'text/css')
            elif filename[-5:] == '.json':
                self.send_header('Content-type', 'application/javascript')
            elif filename[-3:] == '.js':
                self.send_header('Content-type', 'application/javascript')
            elif filename[-4:] == '.ico':
                self.send_header('Content-type', 'image/x-icon')
            else:
                self.send_header('Content-type', 'text/html')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            try:
                with open(filename, 'rb') as fh:
                    html = fh.read()
                    self.wfile.write(html)
            except:
                return

        ## creates chatbot responses
        if parsedPath[2] == '/chat':
            msg = query.split('=')[1]
            self.end_headers()

            # chatbot that does a to-do list
            if 'ajoute' in msg.lower():
                liste.append(msg.split('ajoute%20')[1])
                self.wfile.write(str.encode("J'ai ajouté '" + msg.split('ajoute%20')[1] + "' à la liste."))

            elif 'affiche' in msg.lower():
                if not liste:
                    self.wfile.write(str.encode("Votre liste est vide"))
                else:
                    self.wfile.write(str.encode("Votre liste:<br>"))
                    for i in range(len(liste)) :
                        self.wfile.write(str.encode(liste[i]+"<br>"))

            elif 'supprime' in msg.lower():
                if msg.split('supprime%20')[1] in liste:
                    liste.remove(msg.split('supprime%20')[1])
                else:
                    self.wfile.write(str.encode(msg.split('supprime%20')[1] + " n'était pas dans la liste"))
                self.wfile.write(str.encode("Votre liste:<br>"))
                for i in range(len(liste)) :
                    self.wfile.write(str.encode(liste[i]+"<br>"))

            elif 'aide' in msg.lower():
                self.wfile.write(str.encode('Pour ajouter quelque chose, dites-moi "ajoute ...". <br>Pour supprimer quelque chose, dites-moi "supprime ...".<br>Pour voir votre liste, dites-moi "affiche".<br>Pour un rappel de ces commandes, dites-moi "aide".'))

            elif "bonjour" in msg.lower():
                self.wfile.write(str.encode("Bonsoir!"))

            else :
                #create a chatterbot chatbot
                frenchBot = ChatBot('TchatBot', read_only=True, storage_adapter='chatterbot.storage.SQLStorageAdapter')

                result = frenchBot.get_response(msg)
                self.wfile.write(str.encode(result.text))

## V1 bonjour/bonsoir server
##        if query == "Bonjour" or query == "bonjour":
##            self.wfile.write(str.encode("Bonsoir"))

httpd = HTTPServer(('',PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()


# Resources
# https://codinginfinite.com/chatbot-in-python-flask-tutorial/
# https://pypi.org/project/ChatterBot/
# https://pypi.org/project/chatterbot-corpus/
