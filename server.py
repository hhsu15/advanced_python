import socket

def main():
	# set up the address
	host = '127.0.0.1'
	port = 5002
   
    # bind socket with addrss
	s = socket.socket()
	s.bind((host, port))
    
	# get the connected client and address
	s.listen(1)
	c, addr = s.accept()

	print("connection from: " + str(addr))
    
	# start the server
	while True:
	    # receive data from client
		data = c.recv(1024).decode('utf-8')
		if not data:
			break
		print('from connected user: '+ data)
		add_res = 'FROM SERVER: '
		data = add_res + data.upper()
		print('sending: ' + data)
		# send response to client
		c.send(data.encode('utf-8'))

	c.close()

if __name__ =='__main__':
	main()
