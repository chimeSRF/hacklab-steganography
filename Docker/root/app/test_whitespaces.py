# Read the input from a text file
with open('res/text.txt', 'r', encoding='utf-8') as file:
    input_string = file.read()

first_whitespace_char = None
decoded_string = ""

for char in input_string:
    if char.isspace():
        if first_whitespace_char is None:
            first_whitespace_char = char
            decoded_string += '0'
        else:
            decoded_string += '0' if char == first_whitespace_char else '1'

# Convert the binary representation to text
binary_chunks = [decoded_string[i:i + 8] for i in range(0, len(decoded_string), 8)]
text = "".join([chr(int(binary_chunk, 2)) for binary_chunk in binary_chunks])

print(text)