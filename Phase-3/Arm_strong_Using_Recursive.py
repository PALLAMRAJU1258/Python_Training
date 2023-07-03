def arm_strong(sum,n,len):
    r=n%10
    sum+=r**len
    n//=10
    if n == 0:
        return sum
    else:
        return arm_strong(sum,n,len)

num = int(input())
if num == arm_strong(0,num,len(str(num))):
    print(num,"is armstrong number")
else:
    print(num,"is not armstrong number")
