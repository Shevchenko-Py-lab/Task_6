from os import path

import requests


FILE_URL = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
FILE_1_NAME = "nginx_logs.txt"


def main(file):
    if not path.exists(FILE_1_NAME):
        download_file()

    parsing_list = file_parser(FILE_1_NAME)
    return parsing_list


def download_file():
    response = requests.get(FILE_URL, stream=True)

    with open(FILE_1_NAME, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            f.write(chunk)


IP_INDEX = 0
TYPE_INDEX = 5
RES_INDEX = 6


def file_parser(file):
    with open(FILE_1_NAME,  encoding='utf-8') as file_1:
        for line in file_1:

            element = line.split()

            remote_addr, request_type, requested_resource = (

                element[IP_INDEX],
                element[TYPE_INDEX],
                element[RES_INDEX]
            )

            request_type = request_type.strip('"')

            yield remote_addr, request_type, requested_resource


print(*main(FILE_1_NAME))
print_text = file_parser(FILE_1_NAME)

# что-то долго отрабатывает подсчёт запросов

ip_address = [ip[0] for ip in print_text]
lst_ip = list(ip_address)
result = {}
for i in ip_address:
    result[i] = lst_ip.count(i)
sorted_ip_frequency = sorted(result.items(), key=lambda element: element[1])
print(f'Спамеры: {sorted_ip_frequency[-5:]}')
