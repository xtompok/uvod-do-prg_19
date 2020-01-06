import pathlib

p = pathlib.Path('/home/jethro/Dokumenty/prifuk/uvod-do-prg_19/cv10/paths.py')
p2 = pathlib.Path('paths.py')
print(p)
for par in p.parents:
    print(par)

# List parent directory of current working directory
p = pathlib.Path.cwd()
adir = p.parent
for file in adir.iterdir():
    if file.is_dir():
        print("Dir {}".format(file))
    else:
        print(file)
print(p.parent)

print()
# Print all files in ./in directory
cwd = pathlib.Path.cwd()
in_dir = cwd / 'in'
for file in in_dir.iterdir():
    print(file)
    with open(file,"r",encoding="utf-8") as f:
        print(f.read())
print(in_dir)