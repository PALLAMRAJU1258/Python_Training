from math import sqrt
def jumpSearch(arr,x,n):
    step = sqrt(n)
    prev = 0
    a = arr[int(min(step,n)-1)]
    print("a is:",a)
    while arr[int(min(step,n)-1)] < x:
              prev = step
              step += sqrt(n)
              print("work")
              if prev >= n:
                  print("not work")
                  return -1
    while arr[int(prev)] < x:
        prev += 1
        if prev == min(step,n):
            return -1
    if arr[int(prev)] == x:
        return int(prev)
    return -1


arr = [0,1,1,2,4,5,9,13,21,34,55,89,144,300,377,710]
x = 55
n = len(arr)
index = jumpSearch(arr,x,n)
print(f"Number {x} at index {index}")
