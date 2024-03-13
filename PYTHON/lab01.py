def arithm_prog(a, d, N): 
    for i in range(N):
        term = a + i*d
        print(term, end=' ')
    return


def calc_factorial(n): 
    if n == 0:
        return 1
    else:
        return n * calc_factorial(n - 1)
    

def calc_min_common_multiple(a, b):
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


def prime_in_range(left, right):
    for num in range(left, right + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                return num


def printSymbolsOverThreshold(file, thresholdToPrint):
    """
    Prints symbols from a file that appear more than a certain number of times.

    Parameters:
    file (str): The path to the file to read.
    thresholdToPrint (int): The minimum number of times a symbol must appear to be printed.

    Returns:
    None
    """
    with open(file, 'r') as file:
        data = file.read().replace('\n', '')
        count_dict = {}
        for i in data:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
        for symbol, count in count_dict.items():
            if count > thresholdToPrint:
                print(symbol)



def main():
   arithm_prog(1, 2, 10)
   print(calc_factorial(5))
   print(calc_min_common_multiple(5, 7)) #confirm
   # print(prime_in_range(10, 20)) #confirm
   printSymbolsOverThreshold('lab01.txt', 10) 

main()