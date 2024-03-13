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

def get_histograma(file):
    data = file
    count_dict = {}
    for i in data:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict

def analise_de_ficheiro(file):
    histo = get_histograma(file)
    print(histo)
    

import chardet
# Function to detect file encoding
def detect_encoding(file_path):
    with open(file_path, 'rb') as f:
        raw_data = f.read()
        result = chardet.detect(raw_data)
        return result['encoding']

# Detect encoding and open file


def anlise_de_ficheiros(folder_name):
    list_files = os.listdir(folder_name)
    print(list_files)
    for file_name in list_files:
        print("------")
        print(file_name)
        file_encoding = detect_encoding(folder_name+"/"+file_name)
       # with open(folder_name+"/"+file_name, 'r',encoding=file_encoding) as file:
        with open(folder_name+"/"+file_name, 'rb') as file:
            file= file.read()
        analise_de_ficheiro(file)
    

anlise_de_ficheiros("TestFilesCD")