from random import randint

LIST_LEN = 100
# Create a list of length LIST_LEN
# with random letters from 'a' to 'z'
searchlist = [chr(randint(ord('a'),ord('z'))) for _ in range(LIST_LEN)]
searchlist.sort()
print(searchlist)

def bin_search(alist, char):
    pass
    # returns True if char in list, else False

def _bin_search(alist,char,left,right):
    # Looks at half of the range
    # If num is there, return True
    # else recurse on the correct side of the list
    pass

bin_search(searchlist,'c')