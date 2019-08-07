import json
import os


class CountryIter:

    def __init__(self, file_from='countries.json', file_to='result.txt'):
        self.file_from = file_from
        self.file_to = file_to

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.file_from, 'r', encoding='utf-8-sig') as data:
            json_data = json.load(data)
            for country in json_data[:]:
                with open(self.file_to, 'a', encoding='utf-8-sig') as result:
                    url = 'https://en.wikipedia.org/wiki/'
                    string = f'{country["name"]["common"]}: {url}{country["name"]["common"].replace(" ", "_")}' + '\n'
                    result.write(string)
            raise StopIteration


def clear_json():
    try:
        os.remove('result.txt')
    except FileNotFoundError:
        pass


if __name__ == '__main__':
    clear_json()
    for item in CountryIter():
        pass
    print('=Done! Check result.txt=')
