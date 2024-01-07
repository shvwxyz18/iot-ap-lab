from gsmmodem.modem import GsmModem
import time
gsm_port = '/dev/ttyUSB0' 
gsm_baudrate = 9600 
phone_number = "+1234567890"
modem = GsmModem(gsm_port, gsm_baudrate)
modem.connect()
modem.dial(phone_number) 
print(f"Calling {phone_number}...")
time.sleep(20)
modem.hangup()
print("debgey annadu")
modem.disconnect()

