"""b = []
def selectionSort(arr):
    k = 0
    for i in range(0,len(arr)):
        k = min(arr)
        b.append(k)
        arr.remove(k)




arr = [20,30,10,50,40]
selectionSort(arr)
for i in b:
    print(i,end=" ")"""





def selection_sort(alist):
    for i in range(0,len(alist)-1):
        smallest = i
        for j in range(i+1,len(alist)):
            if alist[j] < alist[smallest]:
                smallest = j
        alist[i],alist[smallest] = alist[smallest],alist[i]



alist = input("Enter the list of numbers:").split()
alist = [int(x) for x in alist]
selection_sort(alist)
for i in range(len(alist)):
    print(alist[i],end=" ")
