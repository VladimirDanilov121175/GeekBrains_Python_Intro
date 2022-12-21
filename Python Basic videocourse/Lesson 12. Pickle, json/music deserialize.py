import pickle
import json

with open('group.json', 'r', encoding='utf-8') as j:
    res = json.load(j)
print(json.dumps(res, indent=4, ensure_ascii=False))

with open('group.pickle', 'rb') as p:
    res = pickle.load(p)
print(res)