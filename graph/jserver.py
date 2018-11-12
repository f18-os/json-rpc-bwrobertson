# minimalistic server example from 
# https://github.com/seprich/py-bson-rpc/blob/master/README.md#quickstart

from node import *
import socket
from bsonrpc import JSONRpc
from bsonrpc import request, service_class
from bsonrpc.exceptions import FramingError
from bsonrpc.framing import (
	JSONFramingNetstring, JSONFramingNone, JSONFramingRFC7464)
import pickle

leaf1 = node("leaf1")
leaf2 = node("leaf2")

root = node("root", [leaf1, leaf2])

# Class providing functions for the client to use:
@service_class
class ServerServices(object):

  @request
  def swapper(self, txt):
    return ''.join(reversed(list(txt)))

  @request
  def nop(self, txt):
    print(txt)
    return txt

  @request
  def inc(self):
    with open('cereal.txt', 'rb') as cerealFile:
      root = pickle.load(cerealFile)

    increment(root)

    with open('cereal.txt', 'wb') as cerealFile:
      pickle.dump(root, cerealFile)
    return

# Quick-and-dirty TCP Server:
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(('localhost', 50001))
ss.listen(10)

while True:
  s, _ = ss.accept()
  # JSONRpc object spawns internal thread to serve the connection.
  JSONRpc(s, ServerServices(),framing_cls=JSONFramingNone)
