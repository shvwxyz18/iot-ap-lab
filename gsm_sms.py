from gsmmodem.modem import GsmModem
import time

# Replace these values with your actual port and baud rate
gsm_port = '/dev/ttyUSB0'  # Example port, adjust as needed
gsm_baudrate = 9600  # Example baud rate, adjust as needed

def send_sms(message, recipient_number):
    modem = GsmModem(gsm_port, gsm_baudrate)
    modem.connect()
    message = 'mg'
    # Send SMS
    modem.send_sms(recipient_number, message)
    print(f"SMS sent to {recipient_number}: {message}")

if __name__ == "__main__":
    # Replace these values with the actual message and recipient number
    message_to_send = "Hello, this is a test SMS from Raspberry Pi!"
    recipient_phone_number = "9398739018"  # Replace with the recipient's phone number
    
    send_sms(message_to_send, recipient_phone_number)
