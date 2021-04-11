import string
import random

# lower_upper_alphabet = string.ascii_letters
# random_letter = random.choice(lower_upper_alphabet)
# print("".join(random.choice(lower_upper_alphabet) for i in range(6)))


def get_random_string(length):
    # Random string with the combination of lower and upper case
    letters = string.ascii_letters
    result_str = "".join(random.choice(letters) for i in range(length))
    print(result_str)

for x in range(168):
    get_random_string(88)