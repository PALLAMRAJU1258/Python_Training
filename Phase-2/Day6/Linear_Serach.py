pos = -1
def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False

list = [100,40,20,10]
n = 200
if search(list,n):
    print("Found it at position",pos+1)
else:
    print("Not Found")
