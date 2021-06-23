import os
import json


dirname = os.path.dirname(__file__)
rawFile = os.path.join(dirname, '../data/twitter/raw.json')
output = os.path.join(dirname, '../data/twitter/processed.json')

with open(rawFile) as file:
    data = json.load(file)
    data = [{'content': att["content"], "lang": att["lang"]} for att in data]

    with open(output, "a", encoding="utf-16") as destination:
        json.dump(data, destination, ensure_ascii=False)
