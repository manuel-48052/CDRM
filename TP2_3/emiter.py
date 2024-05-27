import serial
import random
import time
from my_checksum import checksum

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
    port = '/dev/ttyS0'  # Porta serial do Raspberry Pi
    baudrate = 9600


    primes = get_primes(15)
    

    
    with serial.Serial(port, baudrate, timeout=1) as ser:
        time.sleep(2)  # Espera para garantir que a conexão está estável
        for prime in primes:
            data = prime.to_bytes(length=2, byteorder="big")
            check_sum = checksum(data).to_bytes(length=2, byteorder="big")
            data  += check_sum
            ser.write(data)
                    
        ser.write(END_OF_TEXT)

        print(f"Sent prime numbers up to {n} to the PC.")

if __name__ == "__main__":
    main()
