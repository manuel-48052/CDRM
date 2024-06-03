import serial
import random
import time
from my_checksum import calculate_ipchecksum

MAX_NUMBER_FOR_WORD = 65535
END_OF_TEXT: bytes = chr(3).encode()

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, (num//2)+1):
        if (num % i) == 0:
            return False
    return True

def get_primes(n):
    primes = []
    for num in range(2, n + 1):
        if num >= MAX_NUMBER_FOR_WORD:
            print(f"n cant be more then {MAX_NUMBER_FOR_WORD}")
            return primes
        if is_prime(num):
            primes.append(num)
    return primes


def main():
    port = '/dev/serial0'  # Porta serial do Raspberry Pi
    baudrate = 9600
    checksumbb = True
   
    with serial.Serial(port, baudrate, timeout=1) as ser:
        data = get_primes(3)
        time.sleep(2)  # Espera para garantir que a conexão está estável
    
        if checksumbb:
            check_sum = calculate_ipchecksum(data)
            #alter data here to simulate error
            #data[0] = 22 #example to simulate error
            data.append(check_sum)
        print(data)
        for number in data:
            number = int.to_bytes(number,length=2, byteorder="big")
            print(number)
            ser.write(number)


        time.sleep(1)
        ser.write(END_OF_TEXT)
        print(f"Sent prime numbers up to {data} to the PC.")


if __name__ == "__main__":
    main()