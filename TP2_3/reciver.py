import serial

def checksum(data):
    print("")

def checksum(data):
    if len(data) != 2:
        raise ValueError("Data must be exactly 2 bytes (16 bits)")

    # Convert bytes to a 16-bit word
    word = (data[0] << 8) + data[1]
    
    # Calculate one's complement of the word
    total = ~word & 0xFFFF
    
    return total


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


def main():
    check_sum = False
    port = 'COM3'  # Porta serial no PC (verifique qual é a correta)
    baudrate = 9600

    with serial.Serial(port, baudrate, timeout=1) as ser:
        print(f"Listening on {port}...")
        data = ser.read(3)  # Ler até 3 byte
        if data:
            prime = data.decode('utf-8')
            if check_sum:
                verify_checksum(prime[0:1],verify_checksum = prime[2])
            print(f"Received primes: {prime}")

if __name__ == "__main__":
    main()
