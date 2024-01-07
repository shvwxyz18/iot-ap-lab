import socket			 
s = socket.socket()		 
port = 12345			
s.connect(('127.0.0.1', port)) 
print (s.recv(1024).decode())
s.close()

#the input from server.py is displayed on this program's terminal
