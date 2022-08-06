# TwoStackQueue Exercise
class TwoStackQueue:
    def __init__(self):
        self.instack = [] # add an item to this stack
        self.outstack = [] # pop an item out of this stack
    def enqueue(self, item):
        self.instack.append(item)
        # TODO - add an item to the queue
        # 3 4 5 6
        # 6 5 4 3 
    def dequeue(self):
        self.outstack = []
        for i in range (len(self.instack)):
            self.outstack.append(self.instack.pop())
        # 1 2 3 4 -> []
        # [] -> 4 3 2 1 
        output = self.outstack.pop()
        
        # 4 3 2 1 -> 4 3 2
        self.instack = []
        for i in range (len(self.outstack)):
            self.instack.append(self.outstack.pop())
        return output
        # 2 3 4
        

q = TwoStackQueue()

q.enqueue("C")
q.enqueue(2)
q.enqueue("A")

print(q.dequeue()) # print C


print(q.dequeue()) # print 2

print(q.dequeue()) # print A



# TwoStackQueue Exercise
class TwoStackQueue2:
    def __init__(self):
        self.instack = [] # add an item to the queue in this stack
        self.outstack = [] # pop an item from the queue out of this stack
    def enqueue(self, item):
        self.instack.append(item)
    def dequeue(self):
        if(len(self.outstack)==0):
            for i in range (len(self.instack)):
                self.outstack.append(self.instack.pop())
        else:
            self.outstack.pop()
        return None # replace this with your code