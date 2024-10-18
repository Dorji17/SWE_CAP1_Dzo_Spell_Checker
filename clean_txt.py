
# from genericpath import isfile
# import re

# def clean_text(input_file, output_file):
#   """read from input_file, clean the text, and write unique lines to output_file"""

# def clean_line(line):
#    """remove unwanted character from the line."""
#    return re.sub(r'[^\u0000-\u0FFF\s]', '', line.strip())

# try:
   
#    with open(input_file, 'r', encoding='utf-8') as outfile: 
#    unique_words = set(clean_line(line)for line in isfile if line.strip())

# import re

# # Function to clean text
# def clean_text(text):
#     # Remove leading and trailing whitespace
#     text = text.strip()
#     # Remove punctuation
#     text = re.sub(r'[^\w\s]', '', text)
#     # Convert to lowercase
#     text = text.lower()
#     # Remove extra spaces
#     text = re.sub(r'\s+', ' ', text)
#     return text

# # Read from the input file, clean the text, and write to the output file
# input_file_path = 'dictionary.txt'  # Replace with your input file path
# output_file_path = 'cleaned_output\.txt'  # Replace with your desired output file path

# with open(input_file_path, 'r', encoding='utf-8') as infile:
#     # Read the entire file
#     content = infile.read()
#     # Clean the text
#     cleaned_content = clean_text(content)

# # Write the cleaned content to a new file
# with open(output_file_path, 'w', encoding='utf-8') as outfile:
#     outfile.write(cleaned_content)

# print("Text cleaning complete. Cleaned file saved as:", output_file_path)

import re

# Function to check if a string contains English characters
def contains_english(text):
    return bool(re.search(r'[a-zA-Z]', text))

# Function to clean the dictionary entries
def clean_dzongkha_dictionary(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as infile:
        cleaned_lines = []
        
        for line in infile:
            # If the line does not contain English characters, keep it
            if not contains_english(line):
                cleaned_lines.append(line)

    # Write cleaned lines to output file
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        outfile.writelines(cleaned_lines)

# File paths
input_file_path = 'dictionary.txt'  # Replace with your input file path
output_file_path = 'cleaned_dzongkha_dictionary.txt'  # Replace with your desired output file path

# Clean the dictionary
clean_dzongkha_dictionary(input_file_path, output_file_path)

print("Cleaning complete. Cleaned file saved as:", output_file_path)