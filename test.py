# 
# test.py 
#   trys a known picture and an unknown picture
#   against the websocker. 
import sys
import websocket  # pip3 install websocket-client
import base64
import json

def get_name(uri, bfr):
  ws = websocket.WebSocket()
  ws.connect(uri, timeout=10)
  ws.send(base64.b64encode(bfr))
  reply = ws.recv()
  ws.close()
  return reply
  
def main():
  # hardcoded for me and my machines and network.
  #host = 'mini.local'
  host = '192.168.1.2'  # bronco.local won't work! BUG somewhere 
  port = 5439
  #uri = f'ws://{host}:{port}'
  uri = f'ws://{host}:{port}/Cnn_Shapes'

  fp = './test_image/person.jpg'
  f = open(fp, 'rb')
  img = f.read()
  f.close()
  rp = json.loads(get_name(uri, img))
  #rp = get_name(uri, img)
  print(f"Person? : {rp['value']} {rp['time']} secs")

  fp = './test_image/notperson.jpg'
  f = open(fp, 'rb')
  img = f.read()
  f.close()
  rp = json.loads(get_name(uri, img))
  #rp = get_name(uri, img)
  print(f"Person? : {rp['value']} {rp['time']} secs")


if __name__ == '__main__':
  sys.exit(main())
