"""(Python) Neste exercício, pretende-se efetuar a análise de fontes de símbolos.
(a) Para todos os ficheiros do conjunto TestFilesCD.zip, apresente: o valor da informação própria de cada símbolo; o
valor da entropia; o histograma. Comente os resultados obtidos.
(b) Considere os ficheiros ListaPalavrasEN.txt e ListaPalavrasPT.txt, os quais contêm listagens de palavras em
Língua Inglesa e Língua Portuguesa, respetivamente. Para cada ficheiro:
(i) Uma estimativa da percentagem de ocorrência de cada símbolo (carater). Indique os cinco símbolos mais frequentes.
(ii) Uma estimativa da percentagem de ocorrência dos pares de símbolos mais frequentes. Indique os cinco pares de
símbolos mais frequentes.
Comente os resultados obtidos"""

import os
import math
from collections import Counter
import matplotlib.pyplot as plt
import secrets
import random

def file_read_simbols(arquivo):
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

def analise_de_ficheiro(arquivo):
    dados = file_read_simbols(arquivo)
    if dados == None:
        return
    contagem = Counter(dados)

    total = sum(contagem.values())

    # Informação própria
    own_info = {k: -math.log2(v/total) for k, v in contagem.items()}

    print("Informação própria:")
    for k, v in own_info.items():
        print(f"{k}: {v:.4f}")

    entropia = -sum(freq/total * math.log2(freq/total) for freq in contagem.values())

    # Plot do histograma
    contagem = sorted(contagem.items())
    simbolos, frequencias = zip(*contagem)
    # probabilidade = [freq/total for freq in frequencias]
    
    plt.bar(simbolos, frequencias)
    plt.title(arquivo)
    print(f"\nEntropia: {entropia:.4f} bit/symbol")
    plt.show()


# Detect encoding and open file


def anlise_de_ficheiros(folder_name):
    list_files = os.listdir(folder_name)
    print(list_files)
    for file_name in list_files:
        print("------")
        print(file_name)
        analise_de_ficheiro(folder_name+"/"+file_name)
        
        
    

#anlise_de_ficheiros("TestFilesCD")

def percentagem_de_ocorrência_de_cada_símbol(arquivo,top=5):
    dados = file_read_simbols(arquivo)

    contagem = Counter(dados)

    total = sum(contagem.values())
   # own_info = {k: -math.log2(v/total) for k, v in contagem.items()} 
    percentag = {k: round(((v/total)*100),2) for k, v in contagem.items()} 
    sorted_percentag = sorted(percentag.items(), key=lambda x:x[1],reverse=True)
    if (len(sorted_percentag)>top):
        for i in range(top):
            print(sorted_percentag[i])
    else:
        for i in range(len(sorted_percentag)):
            print(sorted_percentag[i])



def pares_de_simblos(arquivo):
    dados = file_read_simbols(arquivo)        
    pares = [dados[i:i+2] for i in range(len(dados)-1)]
    frequencia = Counter(pares)
    print(frequencia.most_common(5))
    return frequencia.most_common(5)



#
#implementação de fontes de símbolos
def vernam_cipher(plaintext, key):
    ciphertext = ''
    for i in range(len(plaintext)):
        char = chr(ord(plaintext[i]) ^ ord(key[i]))
        ciphertext += char
    return ciphertext

def vernam_decrypt(ciphertext, key):
    decrypted_text = ''
    for i in range(len(ciphertext)):
        char = chr(ord(ciphertext[i]) ^ ord(key[i]))
        decrypted_text += char
    return decrypted_text

def generate_random_key(length):
    return ''.join(secrets.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for i in range(length))

# def generate_sequence(N, probabilities):
#     """
#     Função que gera uma sequência de N símbolos de acordo com as probabilidades
#     definidas na FMP.
#     """
#     symbols = []
#     for i in range(N):
#         symbol = np.random.choice(len(probabilities), p=probabilities)
#         symbols.append(symbol)
#     return symbols

def bsc(seq, p):
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

def ex_5():
    arquivo = "Grayscale Images/bird.gif"
    with open(arquivo, 'rb') as f:
        dados = f.read()
    print(dados[0])

    from PIL import Image
    import io
    image = Image.open(io.BytesIO(dados))
    image.show()
     
    


    

def bsc_str(input: str, p: float) -> str:
    transit: list[str] = [c for c in input]
    for i in range(len(transit)):
        if random.random() < p:
            transit[i] = "0" if input[i] == "1" else "1"
    return transit

def bsc_ints(seq, p):
    output_s = ""
    for leter in seq:
        leter_bin = format(leter, 'b').rjust(8, '0')      
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

def ber(seq1, seq2):
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


def ex_6():
    print("ex 6")

   # with open("TestFilesCD/a.txt", 'r') as file: 
    arquivo = "TestFilesCD/a.txt"
    dados = file_read_simbols(arquivo)
    length = len(dados)      
    the_key_random = generate_random_key(length)
    
    #chave constante
    
    print(dados)
    output_bits = bsc(dados, 0.1)
    print(output_bits)
    
    print(f"BER: {ber(dados,output_bits)}")


if __name__ == "__main__":
    # Exibe um menu de opções para o usuário
    print("Escolha uma opção:")

    
    # Recebe a entrada do usuário
    opcao = input("Digite o número da opção desejada: ")
    if opcao == "3a":
        folder_name = "TestFilesCD"
        file_name = "abbccc.txt"
        anlise_de_ficheiros(folder_name)
    elif opcao == "3b":
        print("top 5 ListaPalavrasPT")
        percentagem_de_ocorrência_de_cada_símbol("ListaPalavrasPT.txt")
        print("top 5 ListaPalavrasEN")
        percentagem_de_ocorrência_de_cada_símbol("ListaPalavrasEN.txt")
    elif opcao == "5":
        print("ex 5")
        ex_5()
    elif opcao == "6":
        print("ex 6")
        ex_6()