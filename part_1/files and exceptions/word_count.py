def count_words_and_letters(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print(f"file {filename} not found or does not exist")
    else:
        num_letters = len(contents.strip())
        num_words = len(contents.split())
        print(f"the file {filename} has {num_words} words and {num_letters} letters")


archives = ['pi_digits.txt', 'programming.txt', 'guests.txt', 'not_exists.txt', 'pi_million_digits.txt']

for archive in archives:
    count_words_and_letters(archive)
