import serial
import random
import time



PRIMES = [5, 11, 17, 29, 37, 41, 53, 59, 67, 71, 97, 101, 127, 149, 179, 191, 223, 227, 251]

def is_prime(num):
    #not used
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_primes(n):
    #not used
    primes = []
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def get_prime_random():
    i = random.randint(0, len(PRIMES)-1)
    return PRIMES[i]



def main():
    port = '/dev/ttyS0'  # Porta serial do Raspberry Pi
    baudrate = 9600


    prime = get_prime_random()
    #TODO
    check_sum = 0

    prime.append(check_sum)
    data = prime.to_bytes(length=2, byteorder="big")
    print(prime)
    print(data)


    with serial.Serial(port, baudrate, timeout=1) as ser:
        time.sleep(2)  # Espera para garantir que a conexão está estável
        ser.write(data)

        print(f"Sent prime numbers up to {n} to the PC.")

if __name__ == "__main__":
    main()
