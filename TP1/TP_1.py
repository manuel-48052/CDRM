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

def file_read_simbols(arquivo):
    if arquivo.endswith('.txt'):
        with open(arquivo, 'r') as f:
            dados = f.read()
        # Process the text data here
    elif arquivo.endswith('.bmp'):
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
        return
    return dados

def analise_de_ficheiro(arquivo):
    dados = file_read_simbols(arquivo)

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
    print(sorted_percentag)
    



folder_name = "TestFilesCD"
file_name = "abbccc.txt"
percentagem_de_ocorrência_de_cada_símbol(folder_name+"/"+file_name)

def pares_de_simblos(arquivo):
    dados = file_read_simbols(arquivo)