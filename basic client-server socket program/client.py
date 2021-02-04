import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#here you can enter the host ip of the remote host as well
#currently the server is assumed to be localhost
host = socket.gethostname()
port = 12345
client.connect((host,port))
msg = client.recv(1024)
client.close()
print(msg.decode('ascii'))
