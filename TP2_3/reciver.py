import serial
from time import sleep
END_OF_TEXT: bytes = chr(3).encode()



def verify_checksum(data, received_checksum):
    if len(data) != 2:
        raise ValueError("Data must be exactly 2 bytes (16 bits)")

    # Convert bytes to a 16-bit word
    word = (data[0] << 8) + data[1]
    
    # Add the received checksum
    total = word + received_checksum
    
    # Add carry if any
    total = (total & 0xFFFF) + (total >> 16)
    
    # The result should be 0xFFFF if the data is correct
    return total == 0xFFFF

def receive_loop(port: str,baudrate:int) -> bytes:
    received_data: bytes = b""
    with serial.Serial(port,baudrate, timeout=1) as ser:
        while True:
            latest_data: bytes = ser.read()
            if latest_data == END_OF_TEXT:
                sleep(
                    0.5
                )  # wait 500ms because it might not be the EOT character and just data
                if ser.in_waiting == 0:
                    break
            received_data += latest_data
    return received_data


def main():
    check_sum = False
    port = 'COM3'  # Porta serial no PC (verifique qual é a correta)
    baudrate = 9600

    recived = receive_loop(port,baudrate)
    if check_sum:
        for i in range(0,len(recived),4):
            data = recived[i:i+1]
            checksum = recived[i+2:i+3]
            print(f"recived {data}  with checksum {checksum}")
            print(f"checksum verification is {verify_checksum(data,checksum)}") 


        


if __name__ == "__main__":
    main()
    
