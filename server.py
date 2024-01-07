import socket		
from w1thermsensor import W1ThermSensor

sensor = W1ThermSensor()
s = socket.socket()		 
port = 12345			

s.bind(('', port))		 
print ("socket binded to %s" %(port)) 

s.listen(5)	 
print ("socket is listening")		 

while True: 
    temp = sensor.get_temperature()
    c, addr = s.accept()	 
    print ('Got connection from',( addr ))
    c.send('Temperature is {}'.format(temp).encode()) 
    c.close()
    break
    
#the VCC must be connected to pin no 2, DATA must be connected to pin no 7 and GND to pin no 9
#the extension of this is the client.py
#run this program and client.py on different terminals, you will be able to see the temp on the terminal of client.py
