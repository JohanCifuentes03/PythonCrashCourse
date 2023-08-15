file = 'guests.txt'
guests = {}

with open(file, 'w') as object_file:
    condition = True
    while condition:
        name = str(input("Enter your name: "))
        language = input("Enter your programming language: ")
        age = int(input("Enter your age: "))
        guests[name] = {'language': language, 'age': age}
        condition_str = input("Do you want to continue? (y/n)")
        if condition_str != 'y':
            condition = False
    str_message = ''
    for k, v in guests.items():
        str_message += 'guest: ' + str(k) + ' information: ' + str(v) + ',\n'
    object_file.write(str_message)
