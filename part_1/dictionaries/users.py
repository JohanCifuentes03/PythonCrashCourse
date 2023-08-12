def printUsersInfo(users):
    for user, userInfo in users.items():
        print("-------")
        print(f"user: {user}")
        for attr, val in userInfo.items():
            print(f"\t{attr}: {val}")


users = {
    'johan123a': {
        'name': 'johan',
        'fullName': 'johan cifuentes',
        'age': 19,
    },

    'danna21': {
        'name': 'danna',
        'fullName': 'danna gonzalez',
        'age': 19
    }
}

printUsersInfo(users)
