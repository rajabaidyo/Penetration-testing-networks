import socket
#server side code
# host = '192.168.43.100'
#assuming the server is the localhost

host = socket.gethostname()
port = 12345
server = socket.socket()
server.bind((host,port))
server.listen(5)
print('server is listening')

while True:
	connect,addr=server.accept()
	print('got connection from : ',str(addr))
	msg = connect.recv(2048)
	print(msg.decode('ascii'))

	msg = 'Hello'
	connect.send(msg.encode('ascii'))
	connect.close()

