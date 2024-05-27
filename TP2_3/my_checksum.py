def checksum(data):
    if len(data) != 2:
        raise ValueError("Data must be exactly 2 bytes (16 bits)")

    # Convert bytes to a 16-bit word
    word = (data[0] << 8) + data[1]
    
    # Calculate one's complement of the word
    total = ~word & 0xFFFF
    
    return total