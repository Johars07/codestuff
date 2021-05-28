import socket
import sys
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8080
srv_sock.bind(("0.0.0.0", int(sys.argv[1])))
print("0.0.0.0", int(sys.argv[1]), "Server up and running")
srv_sock.listen(5)
print(host)
print("waiting for any incoming connections ....")
cli_sock, cli_addr = srv_sock.accept()
cli_addr_str = str(cli_addr)
print("Client" + cli_addr_str + "Has connected to the server")

filename = input(str("please enter the file name of the file : "))
file = open(filename, 'rb')
file_data = file.read(1024)
cli_sock.send(file_data)
print("Data has been transmitted succesfully")
