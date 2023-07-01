def bubblesort(list):
    for i in range(len(list)-1,0,-1):
        print("value of i:")
        print(i)
        print("The values of j:")
        for j in range(i):
            print(j,end=" ")
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
        print()

list = [10,5,-3,-2,0,100,10]
bubblesort(list)
print(list)
