def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for k, v in user_info.items():
        profile[k] = v


condition = True
users = []
while condition:
    name = str(input("add name: "))
    lastName = str(input("add last name: "))
    optional = True
    while optional:
        optional_input = str(input("Would you like to add something  else? (y/n) "))
        if optional_input == 'n':
            optional = False
        else:
            attr = str(input("Enter the attribute: "))
            value = str(input("Enter the value: "))

