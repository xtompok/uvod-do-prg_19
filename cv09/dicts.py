a1 = {"wheels": 4, "power": 30, "max_speed": 120}
a2 = {"wheels": 4, "power": 100, "max_speed": 50, "blinker": 2}
print(a1)
print(a2)
print(a1["wheels"])
a1["wheels"] = 5
a1["blinker"] = 3
print(a1)
if "blinker" in a2:
    print("Blinkers: ",a2["blinker"])