#  MERGE SORT
#  RUNTIME: n log n
#  STABLE

from heapq import merge


def mergeSort(list):
    if (len(list) == 1):
        return list
    else:
        halfIndex = len(list)//2
        
        a = list[0:halfIndex]
        b = list[halfIndex:len(list)]
        a = mergeSort(a)
        b = mergeSort(b)
        return merge(a,b)

def merge(left,right):
    mergedList = []
    aIndex = 0
    bIndex = 0
    while (aIndex < len(left) and bIndex< len(right)):
            if left[aIndex] <= right[bIndex]:
                mergedList.append(left[aIndex])
                aIndex +=1
            elif (right[bIndex] <= left[aIndex]):
                mergedList.append(right[bIndex])
                bIndex +=1
    while(aIndex < len(left)):
            mergedList.append(left[aIndex])
            aIndex += 1
    while(bIndex < len(right)):
            mergedList.append(right[bIndex])
            bIndex += 1
    return mergedList

print(mergeSort([10,8,5,11,2,10,5,0,2,6,3,13,21,0,3]))
# print(mergeSort([4,1]))
print(merge([8,10],[5,11]))

