import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Google.com - 216.58.209.132
##services.groupkt.com/country/get/iso2code/IN - rest service to pull country details
#mysock.connect(('216.58.209.132', 80))

mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
mysock.send(cmd)

while TRUE:
	data = mysock.recv(512)
	if len(data) < 1: 
		break
	print(data.decode())	

mysock.close()
