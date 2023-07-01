pos = -1
def search(list,n):
    l = 0
    u = len(list) -1
    while l <= u :
        mid = (l+u)//2
        if list[mid] == n:
            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

list = [5,10,15,100]
n = 167
if search(list,n) :
    print("Found it at position",pos+1)
else:
    print("Not Found")
