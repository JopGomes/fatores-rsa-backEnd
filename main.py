import http.server
from urllib.parse import urlparse, parse_qs
from core.schemas.primo import *
from database.db import BancoDados
import json 



class MyRequestHandler(http.server.BaseHTTPRequestHandler):

  def do_GET(self):
    parsed_url = urlparse(self.path)
    params = parse_qs(parsed_url.query)

    if 'numero' in params:
        numero = int(params['numero'][0])
        db = BancoDados()
        result = get_primo(numero, db)   
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(result).encode())

    else:
        self.send_response(400)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Parametro "numero" ausente'.encode('utf-8'))

def get_primo(number = int, db = BancoDados):
    primo = db.buscarFatores(n=number)

    if not primo:
        output = {
            "fator1":-1,
            "fator2":-1,
            "produto":-1,
            "success": False
            }
        return json.dumps(output)
    output = {
            "fator1":primo[0],
            "fator2":primo[1],
            "produto":primo[2],
            "success": True
            }
    return json.dumps(output)

    
   # Criar e iniciar o servidor HTTP
server_address = ('', 8000)
httpd = http.server.HTTPServer(server_address, MyRequestHandler)
print('O servidor foi iniciado')
httpd.serve_forever()