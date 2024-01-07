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
