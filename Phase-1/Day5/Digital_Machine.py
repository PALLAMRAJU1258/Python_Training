__file__='E:\\Day5\\digital_machine.py'
len_bin=int(input())
bin=input()
count=1
for i  in range(1,len_bin-1):
    if (bin[i:i+2]=="11"):
        count+=1
print(count)

