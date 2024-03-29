# minimalistic client example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart
from node import *
import socket
from bsonrpc import JSONRpc
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
import pickle, json

#defining nodes
leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf2])


# Cut-the-corners TCP Client:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 50001))

rpc = JSONRpc(s,framing_cls=JSONFramingNone)
server = rpc.get_peer_proxy()
# Execute in server:
#result = server.swapper('Hello World!')
# "!dlroW olleH"
#print(result)

#print(server.nop({1:[2,3]}))
root.show()
with open('cereal.txt', 'wb') as cerealFile:
	pickle.dump(root, cerealFile)
server.inc()
with open('cereal.txt', 'rb') as cerealFile:
	root = pickle.load(cerealFile)

root.show()

x = convert(root)
y = json.dumps(x)

with open('request.json', 'w') as jsonFile:
    json.dump(y,jsonFile)

rpc.close() # Closes the socket 's' also


