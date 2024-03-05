import json


def cutter(str):
    last_two_chars = str[-2:]
    if last_two_chars[-1].isdigit():
        return str[:-2]
    else:
        return str


with open('tramwaje.json', "r", encoding='utf-8') as read_file:
    data = json.load(read_file)

    print(data['tramwaje'][0]['przystanek'][0]['nazwa'])
    print(data)
    new_dictionary = {}

    for i in data["tramwaje"]:
        new_turple = ()
        new_dictionary[int(i["linia"])] = []
        for j in i["przystanek"]:
            new_turple+= (cutter(j["nazwa"]),)
        new_dictionary[int(i["linia"])].append(new_turple)
    for key,value in new_dictionary.items():
        print(key,value)
    with open('tramwaje_out.json', 'w', encoding='utf-8') as file:
        json.dump(new_dictionary, file, ensure_ascii=False)