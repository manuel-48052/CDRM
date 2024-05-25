import random

def bsc(seq, p):
    """
    This function simulates a binary symmetric channel.
    It takes a sequence of characters and a probability 'p' as input.
    Each bit in the sequence is flipped with probability 'p'.
    The function returns the output sequence.
    """
    output_s = ""
    for leter in seq:
        leter_bin = format(ord(leter), 'b').rjust(8, '0')    
        bits = []
        for bit in leter_bin:
            # Extract the i-th bit using bitwise operations
           # bit = (leter_bin >> i) & 1
            if random.random() < p:
                bits.append(int(bit) ^ 1)
            else:
                bits.append(int(bit))

        bit_str = ''.join(str(bit) for bit in bits)
        output_int = int(bit_str, 2)
        output_s += chr(output_int)

    return output_s

def bsc_arr_int(seq, p):
    """
    This function simulates a binary symmetric channel.
    It takes a sequence of characters and a probability 'p' as input.
    Each bit in the sequence is flipped with probability 'p'.
    The function returns the output sequence.
    """
    output = []

    for bit in seq:
            # Extract the i-th bit using bitwise operations
           # bit = (leter_bin >> i) & 1
            if random.random() < p:
                output.append( 0 if bit else 1)
            else:
                output.append(bit)

    return output

def file_read_simbols(arquivo):
    """
    Read the contents of a file based on its extension.
    
    Args:
        arquivo (str): The path to the file.

    Returns:
        str: The contents of the file.
    """
    if arquivo.endswith('.txt'):
        with open(arquivo, 'r') as f:
            dados = f.read()
        # Process the text data here
    elif arquivo.endswith('.bmp'):
        with open(arquivo, 'rb') as f:
            dados = f.read()
    elif arquivo.endswith('.gif'):
        with open(arquivo, 'rb') as f:
            dados = f.read()
        # imagem = Image.open(arquivo)
        # Process the BMP image data here
    elif arquivo.endswith('.c') or arquivo.endswith('.java') or arquivo.endswith('.htm')or arquivo.endswith('.kt'):
        with open(arquivo, 'r') as f:
            dados = f.read()
    else:
        print("Formato de arquivo não suportado.")
        print(arquivo)
        return None
    return dados


def ber(seq1, seq2):
    """
    This function calculates the Bit Error Rate (BER) between two sequences.
    The sequences are first converted to binary, and then the BER is calculated as the number of differing bits divided by the total number of bits.
    """
    def tobits(s):
        result = []
        for c in s:
            bits = bin(ord(c))[2:]
            bits = '00000000'[len(bits):] + bits
            result.extend([int(b) for b in bits])
        return result
    
    a = tobits(seq1)
    b = tobits(seq2)

    diff_bits = 0

    for i in range(len(a)):
        diff_bits += a[i] ^ b[i]
        
    print("diferent bits")
    print(diff_bits)
    return diff_bits / len(a)

def codify_string_to_bits_3_1(input):    
    bits = []
    for leter in input:
        leter_bin = format(ord(leter), 'b').rjust(8, '0')
        for bit in leter_bin:
            bits.append(int(bit))
            bits.append(int(bit))
            bits.append(int(bit))
    
    return bits



def codify_string_to_itns_7_4(input):
    # m0 m1 m2 m3 p0 p1 p2
    # p0 = m1 m2 m3
    # p1 = m0 m1 m3
    # p2 = m0 m2 m3
    cont_bit = 0
    bits = []
    for leter in input:
        leter_bin = format(ord(leter), 'b').rjust(8, '0')            
        for bit in leter_bin:
            bits.append(int(bit))
            cont_bit +=1
            if cont_bit == 4:               
                cont_bit = 0
                # p0 = m1 m2 m3
                if(bits[-3] ^ bits[-2] ^ bits[-1]):
                    bits.append(1)
                else:
                    bits.append(0)
                # p1 =  m0 m1 m3
                if(bits[-5] ^ bits[-4] ^ bits[-2]):
                    bits.append(1)
                else:
                    bits.append(0)
                # p2 = m0 m2 m3
                if(bits[-6] ^ bits[-4] ^ bits[-3]):
                    bits.append(1)
                else:
                    bits.append(0)
    return bits

def decodify_string_to_itns_7_4(input):
    # m0 m1 m2 m3 p0 p1 p2
    # p0 = m1 m2 m3
    # p1 = m0 m1 m3
    # p2 = m0 m2 m3
    i = 0
    output = []
    
    while i < len(input):
        part = input[i:i+7]
        partb = part
        erro2 = 0
        erro1 = 0
        erro0 = 0
        # p0 = m1 m2 m3
        p0 = (part[0] ^ part[2] ^ part[3])
        p1 = (part[0] ^ part[1] ^ part[3])
        p2 = (part[1] ^ part[2] ^ part[3])
        if(p2 != part[4]):
            #print("error erro1")
            erro2 = 1
        # p1 = m0 m1 m3   
        if(p1 != part[5]):
            #print("error erro2")
            erro1 = 1    
        # p2 = m0 m2 m3    
        if(p0 != part[6]):
            #print("error erro3")
            erro0 = 1
        if(erro0 or erro1 or erro2):
            #print(f"sindroma {erro2} {erro1} {erro0} ")  

            if ((erro2 == 0) & (erro1 == 1) & (erro0 == 1)):
                part[0] = 0 if (part[0] ==1) else 1

            elif ((erro2 == 1) & (erro1 == 1) & (erro0 == 0)):
                part[1] = 0 if (part[1] ==1) else 1

            elif ((erro2 == 1) & (erro1 == 0) & (erro0 == 1)):
                part[2] = 0 if (part[2] ==1) else 1

            elif ((erro2 == 1) & (erro1 == 1) & (erro0 == 1)):
                part[3] = 0 if (part[3] ==1) else 1

            #else:                
                #print("erro em bit de paridade")  
           
        j = 0
        while j < 4:
            output.append(part[j])
            j += 1

        i = i + 7
    return output


def decodify_string_to_itns_3_1(input):
    i = 0
    output = []    
    while i < len(input):
        part = input[i:i+3]
        n = 0
        for numb in part:
            n += numb
        if n < 2:
            output.append(0) 
        else:
            output.append(1) 
        i = i + 3
    return output

def arr_bit_to_str(input):
    i = 0
    output_s = ""
    while i< len(input):
        leter = input[i:i+8]
        binary_string = ''.join(map(str, leter))
        decimal_value = int(binary_string, 2)  # Convert binary string to decimal value
        if 0 <= decimal_value <= 255:  # Check if ASCII value is valid
            ascii_char = chr(decimal_value)
            output_s += ascii_char
        else:
            output_s += '?'  # Invalid ASCII character, replace with '?'
        
        i+=8
    string = ''.join(output_s)
    return string

def ber_lists_ints(seq1, seq2):
    """
    This function calculates the Bit Error Rate (BER) between two sequences.
    The sequences are first converted to binary, and then the BER is calculated as the number of differing bits divided by the total number of bits.
    """
    diff_bits = 0

    for i in range(len(seq1)):
        diff_bits += seq1[i] ^ seq2[i]
    print("diferent bits")
    print(diff_bits)
    return diff_bits / len(seq1)

#1 a) i 
#arquivo = "TestFilesCD/alice29.txt"
#dados = file_read_simbols(arquivo)
#output_bits = bsc(dados, 0.001) 
#print(f"BER: {ber(dados,output_bits)}")

random.seed(1)
BER = 0.03
#1 a) ii 
print("3 1")
arquivo = "TestFilesCD/alice29.txt"
dados = file_read_simbols(arquivo)
rr = codify_string_to_bits_3_1(dados)
output_bits = bsc_arr_int(rr, BER) 
print(f"BER befor correction : {ber_lists_ints(rr,output_bits)}")
r = decodify_string_to_itns_3_1(output_bits)
rrr = arr_bit_to_str(r)
print(f"BER after correction: {ber(dados,rrr)}")#

##1 a) iii
#print("7 4")
#arquivo = "C:/Users/USER/source/repos/CD_2/CDRM/TP2/TestFilesCD/abbccc.txt"
#dados = file_read_simbols(arquivo)
#rr = codify_string_to_itns_7_4(dados)
#output_bits = bsc_arr_int(rr, BER) 
#print(f"BER befor correction : {ber_lists_ints(rr,output_bits)}")
#r = decodify_string_to_itns_7_4(output_bits)
#rrr = arr_bit_to_str(r)
#print(f"BER after correction: {ber(dados,rrr)}")


#2 
def burst_arr_int(seq, p, L):
    """
    This function simulates a burst error model.
    It takes a sequence of bits, a probability 'p' for starting a burst,
    and a burst length 'L'. When a burst starts, it flips 'L' consecutive bits.
    The function returns the output sequence.
    """
    output = []
    i = 0

    while i < len(seq):
        if random.random() < p:
            # Introduce a burst error of length L
            burst_length = min(L, len(seq) - i)  # Ensure we don't go out of bounds
            for j in range(burst_length):
                output.append(0 if seq[i] else 1)
                i += 1
        else:
            output.append(seq[i])
            i += 1

    return output
random.seed(1)
BER = 0.03
#2
print("3 1")
arquivo = "TestFilesCD/alice29.txt"
dados = file_read_simbols(arquivo)
rr = codify_string_to_bits_3_1(dados)
#output_bits = bsc_arr_int(rr, BER) 
output_bits = burst_arr_int(rr, BER,2) 
print(f"BER befor correction : {ber_lists_ints(rr,output_bits)}")
r = decodify_string_to_itns_3_1(output_bits)
rrr = arr_bit_to_str(r)
print(f"BER after correction: {ber(dados,rrr)}")#

