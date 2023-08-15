file = 'information.txt'
with open(file) as file_text:
    lines = file_text.read()

information_string = ''
for line in lines:
    information_string += line

modified_string = information_string.replace(('python' or 'Python'), 'C')

print(modified_string)