# Задание 2
import hashlib


def get_md5(file):
    with open(file, 'r', encoding='utf-8-sig') as doc:
        for _ in doc:
            line_hash = hashlib.md5(doc.readline().encode('utf-8-sig')).hexdigest()
            yield line_hash


if __name__ == '__main__':
    # Используем result.txt, полученный в main.py
    for line in get_md5('result.txt'):
        print(line)
