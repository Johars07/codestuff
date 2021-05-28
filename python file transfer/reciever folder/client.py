import socket
import sys
from utils import recvfile, sendfile, listDir

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_addr = (sys.argv[1], int(sys.argv[2]), sys.argv[3])
srv_addr_str = str(srv_addr)

print("Connecting to " + srv_addr_str + "...")
cli_sock.connect(srv_addr)
print("Connected to file transfer and file lisitng program")
if sys.argv[3] == "get":
    recvfile()
elif sys.argv[3] == "put":
    sendfile()
elif sys.argv[3] == "list":
    listDir()

