# selection and insertion sort
 


def findMinindex(list,start,end):
    minIndex = 0
    for i in range (start,end):
        if (list[minIndex] > list[i]):
            minIndex = i
    return minIndex
 
 
def selectionSort (list):
    for i in range (len(list)):
        minAtP = findMinindex(list,i,len(list)-1)
        # swapping
        temp = list[i]
        list[i] = list[minAtP]
        list[minAtP] = temp
    return list
 
print(selectionSort([5,3,21,7,32,1]))
 
 

# this is  a stable sorting algorthism
def insertionSort(list):
    for p in range (1,len(list)):
        currIndex = p
        while(list[currIndex]<list[currIndex-1] and currIndex != 0):
            temp = list[currIndex-1]
            list[currIndex-1] = list[currIndex]
            list[currIndex] = temp
            currIndex = currIndex-1 
    return list
 
 
 
print(insertionSort([5,3,21,7,32,1]))
print(insertionSort([4,1,8,32,521,3,6]))
print(insertionSort([4,1,8,32,521,3,6]))
print(insertionSort([1,6,3,16,42,31,2,36,15]))

x = 1
x-=1
print(x)