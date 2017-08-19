import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Google.com - 216.58.209.132
##services.groupkt.com/country/get/iso2code/IN - rest service to pull country details
mysock.connect(('216.58.209.132', 80))
mysock.close()
