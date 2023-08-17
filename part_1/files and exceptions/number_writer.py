import json

numbers = [i for i in range(1, 11)]
filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)