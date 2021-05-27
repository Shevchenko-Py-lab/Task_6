import sys
from itertools import zip_longest


def user_hobbies(users_f, hobbies_f, output_f):
    with open(users_f, 'r', encoding='utf-8') as users, \
            open(hobbies_f, 'r', encoding='utf-8') as hobbies, \
            open(output_f, 'a', encoding='utf-8') as output:

        for names, hobby in zip_longest(users, hobbies):
            if names is None:
                exit(1)
            else:
                names = names.strip()
                names = names.replace(',', ' ')
                if hobbies is not None:
                    try:
                        hobbies = hobby.strip()
                        output.write(f'{names}: {hobbies}\n')
                    except AttributeError as e:
                        output.write(f'{names}: "None"\n')


if __name__ == '__main__':
    _script_name, users_file, hobbies_file, output_file = sys.argv
    user_hobbies(users_file, hobbies_file, output_file)
