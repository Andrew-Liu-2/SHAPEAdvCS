#https://courseworks2.columbia.edu/courses/162921/pages/day-3-heap-exercises

# HEAPS
# type of priority queue

# stack: LIFO
# queue: FIFO
# heap: first in best out


# heap sort     

    # binary heap
    # methods: 
    # insert aka heappush - O(log n)
    # delete Min aka heap pop - O(log n)
    # getMin() - O(1)


    # binary tree
    # each parent node has at most two child nodes

    # there are levels in the tree
    # they are represented in a list
    # has to obey heap order property
        # for each node, all entries in the subtree under the node must be greater than the node

    # how do we implement insert and delete?

        # insert
        # comparing value to the parent and swap if less than

            # how do you know which is the parent node in the array?
            # left child  = 2i
            # right child = 2i + 1

            # parent = floor (i/2)
import math


def heapPush(heap, x):
    heap.append(x)
    xIndex = len(heap)-1
    parentIndex = xIndex//2
    while(xIndex != 1 and heap[xIndex]<heap[parentIndex]):
        # swapping
        temp = heap[parentIndex]
        heap[parentIndex] = heap[xIndex]
        heap[xIndex] = temp
        # swapping the indices
        xIndex = parentIndex
        parentIndex = xIndex//2
    return heap

print(heapPush([None,2,3,4,7],0))


        # delete
        # min is at index 1

def heapPop(heap):
    x = heap.pop(1)
    heap[1] = heap[-1]
    heap[-1] = None
    currIndex = 1

    while anyChildren(heap,currIndex) and (childrenSmaller(heap,currIndex)) :
        #find the index of smallest child
        minIndex = smallerChildrenIndex(heap,currIndex)
        
        # switch the min and the curr
        temp = heap[currIndex]
        heap[currIndex] = heap[minIndex]
        heap[minIndex] = temp

        temp == currIndex
        currIndex = minIndex
        minIndex = currIndex
    return x
print(heapPop([0,2,4,7,3]))

def anyChildren(heap, parentIndex):
    child1 = parentIndex *2
    return child1 < len(heap)

# this assumes that there are childeren to compare
def childrenSmaller(heap,parentIndex):
    if(anyChildren == False):
        return False
    child1 = parentIndex * 2
    child2 = parentIndex * 2 + 1
    child2Exist = True
    if (len(heap) <= child2):
        child2Exist = False
        if(heap[parentIndex] > heap[child1]):
            return True
        else:
            return False
    elif (child2Exist):
        if(heap[parentIndex] > heap[child1] or heap[parentIndex] > heap[child2]):
            return True
        else:
            return False

# this assumes there are children smaller  
def smallerChildrenIndex(heap,parentIndex):
    child1 = parentIndex * 2
    child2 = parentIndex * 2 + 1
    child2Exist = True
    # checks if there is a second children
    if(len(heap)<=child2):
        child2Exist = False
        return child1
    else:
        if(heap[child1] < heap[child2]):
            return child1
        elif(heap[child1] >= heap[child2]):
            return child2

    


        # how do we restrucutre?
            # move last entry to root (first level), swap that value with the samller of its children, until 
            # both children are greater

    # height of complete binary tree with N nodes is log N

    # if you insert an underordered list and insert and delete elements

    # each delete element will take log n
    # since there are n elements, the total time is n log base 2 n -> but in big o notation coeeficents dont
    # matter, so n log n
    # you are delete the elements in minimum order
    # giving you an ordered list at the end


    # heap sort is as efficient as merge sort
    # heap sort is not stable however

    # having NONE as the heap's first element is useful


# import heapq as hq
# heap = []

# hq.heappush(heap, 4)
# hq.heappush(heap, 5)
# hq.heappush(heap, 3)
# hq.heappush(heap, 10)
# hq.heappush(heap, 3)
# hq.heappush(heap, 1)
# hq.heappush(heap, 3)
# # hq.heappop()

# print(heap)
# for i in range (len(heap)):
#     print(hq.heappop(heap))

# li = [ 3, 6, 1, 3]
# hq.heapify(li)
# print(li)



