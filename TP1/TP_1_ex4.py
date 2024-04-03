import random
import math
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

#generated_sequence = generate_symbols(fmp, n)
#source_entropy = entropy(fmp.values())
#sequence_entropy = entropy([generated_sequence.count(symbol)/n for symbol in fmp.keys()])

#print("Generated sequence:", generated_sequence)
#print("Sequence entropy:", sequence_entropy)
#print("Source entropy:", source_entropy)


#4bi)
fmp_pins = {'0': 0.1, '1': 0.1, '2': 0.1, '3': 0.1, '4': 0.1, '5': 0.1, '6': 0.1, '7': 0.1, '8': 0.1, '9': 0.1}
pw_generated_sequence = generate_symbols(fmp_pins, 4,6)
pw_source_entropy = entropy(fmp.values())
pw_sequence_entropy = entropy([pw_generated_sequence.count(symbol)/n for symbol in fmp_pins.keys()])

print("4b) i):")
print("Generated sequence:", pw_generated_sequence)
print("Sequence entropy:", pw_source_entropy)
print("Source entropy:", pw_sequence_entropy)
print("\n")



#4bii)
fmp_eurom_nums = {str(num): 1/50 for num in range(1, 51)}
eurom_nums_generated_sequence = generate_symbols(fmp_eurom_nums, 5, 0)
eurom_nums_source_entropy = entropy(fmp.values())
eurom_nums_sequence_entropy = entropy([eurom_nums_generated_sequence.count(symbol)/n for symbol in fmp_eurom_nums.keys()])

print("4b) ii):")
print("Generated sequence:", eurom_nums_generated_sequence)
print("Sequence entropy:", eurom_nums_source_entropy)
print("Source entropy:", eurom_nums_sequence_entropy)
print("")

fmp_eurom_stars = {str(num): 1/12 for num in range(1, 12)}
eurom_stars_generated_sequence = generate_symbols(fmp_eurom_stars, 2, 0)
eurom_stars_source_entropy = entropy(fmp.values())
eurom_stars_sequence_entropy = entropy([eurom_stars_generated_sequence.count(symbol)/n for symbol in fmp_eurom_stars.keys()])

print("Generated sequence:", eurom_stars_generated_sequence)
print("Sequence entropy:", eurom_stars_source_entropy)
print("Source entropy:", eurom_stars_sequence_entropy)
print("\n")

print("4b) iii): strong passwords have Uppercase, lowercase, numbers and special characters")

uppercase_letters_ascii = {}
for letter in range(ord('A'), ord('Z')+1): # +1 because the value is exclusive; ord returns the ascii character of a letter
    uppercase_letters_ascii[chr(letter)] = letter
#print(uppercase_letters_ascii)

fmp_upc_letters = {chr(letter): 1/26 for letter in uppercase_letters_ascii.values()}
print(fmp_upc_letters)

lowercase_letters_ascii = {}
for letter in range(ord('a'), ord('z')+1): # +1 because the value is exclusive; ord returns the ascii character of a letter
    lowercase_letters_ascii[chr(letter)] = letter
#print(lowercase_letters_ascii)

fmp_lwc_letters = {chr(letter): 1/26 for letter in lowercase_letters_ascii.values()}
print(fmp_lwc_letters)



