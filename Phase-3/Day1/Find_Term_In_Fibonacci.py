def fib(n,start=0,next=1,flag=1):
    if n == flag:
        return start
    if n == 1:
        return 0
    else:
        start,next = next,start+next
        return fib(n,start,next,flag+1)


num = int(input())
print(fib(num))