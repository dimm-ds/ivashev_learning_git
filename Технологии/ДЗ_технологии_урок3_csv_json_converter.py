import json
import csv


def csv_json_converter(filename: str, new_file: bool = False) -> str:
    data_1 = []
    with open(f'{filename}.csv', encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        dict_keys = data[0]
        for element in data[1:]:
            dct = {}
            for k, v in zip(dict_keys, element):
                dct[k] = v
            data_1.append(dct)
    if new_file:
        with open(f'{filename}.json', 'w') as f1:
            json.dump(data_1, f1)

    return json.dumps(data_1[:10], indent=4)


print(csv_json_converter('AppleStore', new_file=True))
