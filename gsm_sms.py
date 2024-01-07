from gsmmodem.modem import GsmModem
gsm_port = '/dev/ttyUSB0' 
gsm_baudrate = 9600 

def send_sms(message, recipient_number):
    modem = GsmModem(gsm_port, gsm_baudrate)
    modem.send_sms(recipient_number, message)
    print("mg")

if __name__ == "__main__":
    message_to_send = "bane extralu dengutunnav ga"
    recipient_phone_number = "9876543210" 
    send_sms(message_to_send, recipient_phone_number)

#the gsm module should be attached to the RaspberryPi and run this program. 
