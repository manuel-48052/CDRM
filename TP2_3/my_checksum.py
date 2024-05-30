def calculate_ipchecksum(int_list):
    # Initialize the checksum to 0
    checksum = 0

    # Sum all 2-byte words
    for number in int_list:
        # Convert the 2-byte sequence to an integer
        value = number
        checksum += value

        # If overflow, wrap around
        if checksum > 0xFFFF:
            checksum = (checksum & 0xFFFF) + 1

    # One's complement of the checksum
    checksum = ~checksum & 0xFFFF
 
    return checksum