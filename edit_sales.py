import sys

LINE_LENGTH = 11


def edit_sales(line_from, new_rec):
    line_from -= 1
    with open('bakery.csv', 'r+', encoding='utf-8') as f:
        f.seek(line_from * LINE_LENGTH)
        if not f.readline():
            print("Not found")
            return
        f.seek(line_from * LINE_LENGTH)
        f.write(f'{new_rec.zfill(10)}')


if __name__ == '__main__':
    _script_name, edit_from_line_from, new_record = sys.argv
    edit_sales(int(edit_from_line_from), new_record)
