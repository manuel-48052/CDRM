import serial

def main():
    port = 'COM3'  # Porta serial no PC (verifique qual é a correta)
    baudrate = 9600

    with serial.Serial(port, baudrate, timeout=1) as ser:
        print(f"Listening on {port}...")
        data = ser.read(1)  # Ler até 1 byte
        if data:
            primes = data.decode('utf-8')
            print(f"Received primes: {primes}")

if __name__ == "__main__":
    main()
