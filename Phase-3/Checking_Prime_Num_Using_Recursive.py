def Prime_Num(n):
    if n == 1:
        return False
    elif n > 1:
        for i in range(2,n):
            if (n%i) == 0:
                return False
    return True


num = int(input())
if Prime_Num(num):
    print(num,"is prime number")
else:
    print(num,"is not prime number")