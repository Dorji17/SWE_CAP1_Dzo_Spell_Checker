##########################################
'https://github.com/Dorji17/SWE_CAP1_Dzo_Spell_Checker.git'
#
#Dorji Lhamo
#SWE'A'
#022403389

import argparse
import re

# Function to load the dictionary from a file and return a set of valid words
def load_dictionary(dictionary_file):
    with open(dictionary_file, 'r', encoding='utf-8') as file:
        return set(line.strip() for line in file if line.strip())

# Function to get the ordinal suffix for numbers (e.g., 1st, 2nd, 3rd)
def ordinal(n):
    return f"{n}{'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')}"

# Function to check spelling of words in the input file against the dictionary
def check_spelling(input_file, dictionary):
    with open(input_file, 'r', encoding='utf-8') as file:
        for line_number, line in enumerate(file, start=1):
            # Using regular expression to split by word boundaries (including punctuation)
            words = re.findall(r'\b\w+\b', line)
            for word_position, word in enumerate(words, start=1):
                # If the word is not found in the dictionary, print the error message
                if word not in dictionary:
                    print(f"Line {line_number}, {ordinal(word_position)} word '{word}' is incorrect.")

# Main function to handle command line arguments and call the spell checking function
def main():
    parser = argparse.ArgumentParser(description='Dzongkha Spell Checker')
    parser.add_argument('input_file', help='Input text file to check spelling')
    parser.add_argument('dictionary_file', help='Dictionary file with valid Dzongkha words')
    args = parser.parse_args()

    # Load the dictionary and input file
    dzongkha_dictionary = load_dictionary(args.dictionary_file)

    # Call the spell checking function
    check_spelling(args.input_file, dzongkha_dictionary)

if __name__ == "_main_":
    main()
