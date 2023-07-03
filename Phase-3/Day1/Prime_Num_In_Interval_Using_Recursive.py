def Prime_Num_In_Interval(n):
    if n == 1:
        return False
    elif n < 1:
        return False
    else:
        for i in range(2, n):
            if (n % i) == 0:
                return False
    return True

start = int(input())
end = int(input())
li=[]
for i in range(start,end+1):
    if Prime_Num_In_Interval(i):
        li.append(i)
    else:
        pass
print(li)