import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('services.groupkt.com/country/get/iso2code/IN', 80))
