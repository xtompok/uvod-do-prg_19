import requests
#API_KEY = "a377d32d67992b29cf7579755aa03c4c"
#https://pastebin.com/VKZjWFgj

API_KEY = "f40772726763822166ee40a11eb469a9"
API_ADDR = "http://api.openweathermap.org/data/2.5/forecast"

params = {
    "q": "Praha",
    "APIKEY": API_KEY,
    "units": "metric"
}

res = requests.get(API_ADDR,params=params)
data = res.json()
print(type(data))
for el in data["list"]:
    print("{} {}deg C {}m/s".format(el["dt_txt"],el["main"]["temp"], el["wind"]["speed"]))