def try_example():
    try:
        #inp = input("Enter number:")
        #x = int(inp)
        print("Converted")
    except ValueError as e:
        print("ValueError!")
        print(dir(e))
        print(e)
    print("Outside")

def to_int(x):
    return int(x)

def get_int_0():
    inp = input("Enter number: ")
    try:
        aint = to_int(inp)
    except ValueError:
        print("{} is not an integer, assuming 0".format(inp))
        aint = 0
    return aint

def get_int(input_str):
    while True:
        int_str = input(input_str)
        try:
            num = int(int_str)
            return num
        except ValueError:
            print("Nebylo zadáno celé číslo")

num = get_int_0()
print(num)
num = get_int("Zadej poloměr Země: ")
print(num)
num = get_int("Zadej poloměr Měsíce: ")
print(num)
