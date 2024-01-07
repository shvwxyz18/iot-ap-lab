from gsmmodem.modem import GsmModem
gsm_port = '/dev/ttyUSB0'  
gsm_baudrate = 9600 
message = "bane extralu dengutunnav ga"
recipient_number = "9398739018"  
modem = GsmModem(gsm_port, gsm_baudrate)
modem.connect()
modem.send_sms(recipient_number, message)
print(f"SMS sent to {recipient_number}: {message}")
modem.disconnect()

#connect the gms module to RaspberryPi and run this program
#the connections are, TXD to pin no 8, RXD to pin no 10, GND to pin no 6 and VCC to pin no 4(refer to gsm modem.png for reference)
