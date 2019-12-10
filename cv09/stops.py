import json

with open("DOP_PID_ZASTAVKY_B.json","r",encoding="utf-8") as f:
    data = json.load(f)

print(data)
print(data['features'][0]['properties']['ZAST_NAZEV'])
print(type(data['features']))

for feat in data['features']:
    print(feat)
    print(feat['properties']['OBJECTID'])

filtered_stops = []
for feat in data['features']:
    if feat['properties']['ZAST_PASMO'] == 'P':
        filtered_stops.append(feat)

out_geojson = {'type': 'FeatureCollection'}
out_geojson['features'] = filtered_stops
with open("stops_out.json","w",encoding="utf-8") as f:
    json.dump(out_geojson, f, indent=2, ensure_ascii=False)
