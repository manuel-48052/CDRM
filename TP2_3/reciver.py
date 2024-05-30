import serial
from time import sleep
from my_checksum import calculate_ipchecksum
END_OF_TEXT: bytes = chr(3).encode()


def receive_loop(port: str,baudrate:int) -> bytes:
    received_data: bytes = b""
    with serial.Serial(port,baudrate, timeout=1) as ser:
        while True:
            latest_data: bytes = ser.read()
            if latest_data == END_OF_TEXT:
                sleep(
                    0.6
                )  # wait 500ms because it might not be the EOT character and just data
                if ser.in_waiting == 0:
                    break
            received_data += latest_data
    return received_data


def main():
    check_sum = True
    port = 'COM5'  # Porta serial no PC (verifique qual é a correta)
    baudrate = 9600
    data = []
    recived = receive_loop(port,baudrate)
    if check_sum:
        for i in range(0,len(recived)-2,2): 
            data.apend(int.from_bytes(recived[i:i+2],byteorder="big"))                     
             
        received_checksum = int.from_bytes(recived[-2:],byteorder="big")
        new_checksum = calculate_ipchecksum(data)
        validation = (new_checksum == received_checksum )    
        print(f"recived {data}") 
        print(f" recived checksum = {received_checksum} and calculated = {new_checksum}")
        print(f"validation is {validation}")
    else:
        for i in range(0,len(recived),2):
            data.apend(int.from_bytes(recived[i:i+2],byteorder="big"))
        print(f"recived {data}")


if __name__ == "__main__":
    main()
    
