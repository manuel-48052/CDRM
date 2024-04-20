import random
import math
import string
# 4a)

import random
import math

def generate_symbols(fmp, min, max, print_data=True):
    symbols = list(fmp.keys())
    probabilities = list(fmp.values())
    sequence = []
    source_entropy = entropy(probabilities)
    
    if min != 0 and max == 0:
        n = min
    else:
        n = random.randint(min, max)

    for _ in range(n):
        symbol = random.choices(symbols, probabilities)[0]
        sequence.append(symbol)
        
    sequence_entropy = entropy([sequence.count(symbol) / n for symbol in symbols])
    
    if print_data:
        print("Entropy of Source:", source_entropy)
        print("Entropy of Sequence:", sequence_entropy)
        print("Generated Sequence:", sequence)

    return sequence

def entropy(probabilities):
    entropy = 0
    for p in probabilities:
        if p != 0:
            entropy += p * math.log2(1/p)
    return entropy

#4ai)
fmp_dice = {'1': 1/6, '2': 1/6, '3': 1/6, '4': 1/6, '5': 1/6, '6': 1/6}
print("4a): lançamento de um dado")
dice_generated_sequence = generate_symbols(fmp_dice, 10000, 0)
print()

#4bi)
fmp_pins = {'0': 0.1, '1': 0.1, '2': 0.1, '3': 0.1, '4': 0.1, '5': 0.1, '6': 0.1, '7': 0.1, '8': 0.1, '9': 0.1}
print("4b) i): códigos PIN entre 4 e 6 algarismos")
pw_generated_sequence = generate_symbols(fmp_pins, 4,6)
print()

def generate_n_pins(n):
    for _ in range(n):
        pin = generate_symbols(fmp_pins, 4, 6, False)
        print(''.join(pin))
    print()

generate_n_pins(10)

#4bii)
print("4b) ii): chaves do jogo de sorte Euro-Milhões")
print("Numbers generator:")
fmp_eurom_nums = {str(num): 1/50 for num in range(1, 51)}
eurom_nums_generated_sequence = generate_symbols(fmp_eurom_nums, 5, 0)
print()


print("Stars generator:")
fmp_eurom_stars = {str(num): 1/12 for num in range(1, 12)}
eurom_stars_generated_sequence = generate_symbols(fmp_eurom_stars, 2, 0)
print()

def generate_n_euromillions(n):
    for _ in range(n):
        nums = generate_symbols(fmp_eurom_nums, 5, 0, False)
        stars = generate_symbols(fmp_eurom_stars, 2, 0, False)
        print("Numbers: " + ' '.join(nums))
        print("Stars: " + ' '.join(stars))
    print()

generate_n_euromillions(10)

print("4b) iii): strong passwords have Uppercase, lowercase, numbers and special characters")

visible_chars = string.ascii_letters + string.digits + string.punctuation
prob = 1/len(visible_chars) # Calculate the probability of each symbol
fmp_password_dict = {char: prob for char in visible_chars} # Create the dictionary

password_dict_generated_sequence = generate_symbols(fmp_password_dict, 8, 12)
print()

def generate_n_passwords(n):
    for _ in range(n):
        password = generate_symbols(fmp_password_dict, 8, 12, False)
        print(''.join(password))

generate_n_passwords(10)

def write_n_passwords_to_file(n, filename):
    with open(filename, 'w') as file:
        for _ in range(n):
            password = generate_symbols(fmp_password_dict, 8, 12, False)
            file.write(''.join(password) + '\n')


write_n_passwords_to_file(1000, 'passwords.txt')