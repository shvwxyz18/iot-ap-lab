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