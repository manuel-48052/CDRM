import random
import math
import string
# 4a)

def generate_symbols(fmp, min, max):
    symbols = list(fmp.keys())
    probabilities = list(fmp.values())
    sequence = []
    if(min != 0 and max == 0):
        n = min
    else:
        n = random.randint(min, max)

    for _ in range(n):
        symbol = random.choices(symbols, probabilities)[0]
        sequence.append(symbol)
    return sequence

def entropy(probabilities):
    entropy = 0
    for p in probabilities:
        if p != 0:
            entropy += p * math.log2(1/p)
    return entropy

fmp = {'A': 0.4, 'B': 0.3, 'C': 0.2, 'D': 0.1}

n = 100
generated_sequence = generate_symbols(fmp, n, 0)
source_entropy = entropy(fmp.values())
sequence_entropy = entropy([generated_sequence.count(symbol)/len(generated_sequence) for symbol in fmp.keys()])

print("Generated sequence:", generated_sequence)
print("Sequence entropy:", sequence_entropy)
print("Source entropy:", source_entropy)
print()


#4bi)
fmp_pins = {'0': 0.1, '1': 0.1, '2': 0.1, '3': 0.1, '4': 0.1, '5': 0.1, '6': 0.1, '7': 0.1, '8': 0.1, '9': 0.1}
pw_generated_sequence = generate_symbols(fmp_pins, 4,6)
pw_source_entropy = entropy(fmp.values())
pw_sequence_entropy = entropy([pw_generated_sequence.count(symbol)/len(pw_generated_sequence) for symbol in fmp_pins.keys()])

print("4b) i): códigos PIN entre 4 e 6 algarismos")
#print("Generated sequence:", pw_generated_sequence)
print("Sequence entropy:", pw_sequence_entropy)
print("Source entropy:", pw_source_entropy)
print()

def generate_n_pins(n):
    for _ in range(n):
        pin = generate_symbols(fmp_pins, 4, 6)
        print(''.join(pin))
    print()

generate_n_pins(10)

#4bii)
fmp_eurom_nums = {str(num): 1/50 for num in range(1, 51)}
eurom_nums_generated_sequence = generate_symbols(fmp_eurom_nums, 5, 0)
eurom_nums_source_entropy = entropy(fmp.values())
eurom_nums_sequence_entropy = entropy([eurom_nums_generated_sequence.count(symbol)/len(eurom_nums_generated_sequence) for symbol in fmp_eurom_nums.keys()])

print("4b) ii): chaves do jogo de sorte Euro-Milhões")
#print("Generated sequence:", eurom_nums_generated_sequence)
print("Numbers generator:")
print("Sequence entropy:", eurom_nums_sequence_entropy)
print("Source entropy:", eurom_nums_source_entropy)
print()

fmp_eurom_stars = {str(num): 1/12 for num in range(1, 12)}
eurom_stars_generated_sequence = generate_symbols(fmp_eurom_stars, 2, 0)
eurom_stars_source_entropy = entropy(fmp.values())
eurom_stars_sequence_entropy = entropy([eurom_stars_generated_sequence.count(symbol)/len(eurom_stars_generated_sequence) for symbol in fmp_eurom_stars.keys()])

#print("Generated sequence:", eurom_stars_generated_sequence)
print("Stars generator:")
print("Sequence entropy:", eurom_stars_sequence_entropy )
print("Source entropy:", eurom_stars_source_entropy)
print()

def generate_n_euromillions(n):
    for _ in range(n):
        nums = generate_symbols(fmp_eurom_nums, 5, 0)
        stars = generate_symbols(fmp_eurom_stars, 2, 0)
        print("Numbers: " + ' '.join(nums))
        print("Stars: " + ' '.join(stars))
    print()

generate_n_euromillions(10)

print("4b) iii): strong passwords have Uppercase, lowercase, numbers and special characters")

visible_chars = string.ascii_letters + string.digits + string.punctuation
prob = 1/len(visible_chars) # Calculate the probability of each symbol
fmp_password_dict = {char: prob for char in visible_chars} # Create the dictionary

password_dict_generated_sequence = generate_symbols(fmp_password_dict, 8, 12)
password_dict_source_entropy = entropy(fmp_password_dict.values())
password_dict_sequence_entropy = entropy([password_dict_generated_sequence.count(symbol)/len(password_dict_generated_sequence) for symbol in fmp_password_dict.keys()])

#print("Generated sequence:", password_dict_generated_sequence)
print("Sequence entropy:", password_dict_sequence_entropy)
print("Source entropy:", password_dict_source_entropy)
print()

def generate_n_passwords(n):
    for _ in range(n):
        password = generate_symbols(fmp_password_dict, 8, 12)
        print(''.join(password))

generate_n_passwords(10)

def write_n_passwords_to_file(n, filename):
    with open(filename, 'w') as file:
        for _ in range(n):
            password = generate_symbols(fmp_password_dict, 8, 12)
            file.write(''.join(password) + '\n')


write_n_passwords_to_file(1000, 'passwords.txt')



