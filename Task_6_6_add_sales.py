import sys


def add_sales(add_record):
    with open('bakery.csv', 'a', encoding='utf-8') as f:
        f.write(f'{add_record.zfill(10)}\n')


if __name__ == '__main__':
    _script_name, price_rec = sys.argv
    add_sales(price_rec)
