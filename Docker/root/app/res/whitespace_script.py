with open('text.txt', 'r', encoding='utf-8') as file:
    input_string = file.read()

first_whitespace_char = None
decoded_string = ""

for char in input_string:
# How do you check if its a whitespace char?
    if char.module:
        if ...:
            ...
            decoded_string += '0'
        else:
            ...

# Convert to text
chunks = [decoded_string[i:i + 8] for i in range(0, len(decoded_string), 8)]
text = "".join([chr(int(chunk, 2)) for chunk in chunks])

print(text)
    