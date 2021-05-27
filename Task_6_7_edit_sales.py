import sys


def add_sale(record):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{record}\n')


if __name__ == '__main__':
    _script_name, price_rec = sys.argv
    add_sale(price_rec)