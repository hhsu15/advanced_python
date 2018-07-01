import socket

def main():
	host = '127.0.0.1'
	port = 5003

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))

	print('server started')

	while True:
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
		print("message from: " + str(addr))
		print("from conncted user: " + data)
		data = data.upper()
		print('sending: ' + data)
		s.sendto(data.encode('utf-8'), addr)

	c.close()

if __name__ == "__main__":
	main()
