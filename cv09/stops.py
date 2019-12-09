import json

with open("DOP_PID_ZASTAVKY_B.json","r",encoding="utf-8") as f:
    data = json.load(f)

print(data)
print(data['features'][0]['properties']['ZAST_NAZEV'])
print(type(data['features']))

print(len(data['features']))

for feat in data['features']:
    print(feat)
    print(feat['properties']['OBJECTID'])
