def arithm_prog(u, r, N): 
    """
    This function prints the first 'N' terms of an arithmetic progression.
    The first term is 'u' and the common difference is 'r'.
    """
    for i in range(N):
        term = u + i*r
        print(term, end=' ')
    return


def calc_factorial(n): 
    """
    This function calculates the factorial of a number 'n' using recursion.
    """
    if n == 0:
        return 1
    else:
        return n * calc_factorial(n - 1)
    

def calc_min_common_multiple(a, b):
    """
    This function calculates the least common multiple (LCM) of two numbers 'a' and 'b'.
    """
    if a > b:
        greater = a
    else:
        greater = b
    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1


def prime_in_range(left, right):
    """
    This function prints all prime numbers in the range from 'left' to 'right' (inclusive).
    """
    for num in range(left, right + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
    return

def printSymbolsOverThreshold(file, thresholdToPrint):
    """
    This function reads a file, counts the occurrence of each symbol, and prints the symbols that occur more than 'thresholdToPrint' percent of the time.
    """
    with open(file, 'r') as file:
        data = file.read().replace('\n', '')
        count_dict = {}
        numLetters = 0
        for i in data:
            numLetters+=1
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1

        for symbol, count in count_dict.items():
            percentage = (count/numLetters)*100
            if  percentage > thresholdToPrint:
                print(symbol + " " + str(percentage) +"%")



def main():
   arithm_prog(1, 2, 10) 
   print(calc_factorial(5)) 
   print(calc_min_common_multiple(8, 4)) 
   print(prime_in_range(10, 20)) 
   printSymbolsOverThreshold('lab01.txt', 10) 

main()