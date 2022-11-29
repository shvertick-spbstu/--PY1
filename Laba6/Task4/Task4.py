import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(file_name) -> list[dict]:
    with open(file_name, encoding="utf-8") as f:
        data = f.readlines()
        counter = -1
        for row in data:
            row = row[:-1] #удаляю символ \n
            row = row.split(",") #преобразовываю строку в список строк
            counter += 1
            data[counter] = row #перезапись
    head = data[0]
    data = data[1:]
    result = []
    for item in data:
        dict_ = {k: v for k, v in zip(head, item)}
        result.append(dict_)
    return result


csv_to_list_dict(INPUT_FILE)
print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
