def Pow_Of_num(p,n):
    if p == 0:
        return 1
    
    return n*Pow_Of_num(p-1,n)

num = int(input())
power = int(input())
print(Pow_Of_num(power,num))
