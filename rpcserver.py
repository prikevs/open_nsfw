import xmlrpclib
import requests
from SimpleXMLRPCServer import SimpleXMLRPCServer
from classify_nsfw import get_score

def Get_Score(args):
    return float(get_score(args.data))

server = SimpleXMLRPCServer(("0.0.0.0", 8000))
print "Listening on port 8000..."
server.register_function(Get_Score, "get_score")
server.serve_forever()
