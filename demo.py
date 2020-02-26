import json

with open("sample.json", "r", encoding="utf-8-sig") as read_file:
    data = json.load(read_file)

for k in data["lesson 1"].keys():
    print(data["lesson 1"][k])
    for i in range(len(data["lesson 1"][k])):
        print(data["lesson 1"][k][i]["question"])