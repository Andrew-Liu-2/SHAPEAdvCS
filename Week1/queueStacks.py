# stacks and queues


# stack
        # methods: push and pop
        # first in last out FILO

    # reverse polish notation

        # normally its operand1 operator operator 2  ex. 5 + 1
        # however reverse polish notation is operand1 operand2 operator ex. 5 3 +
        # the advantage is that order is clear: 2 3 + 4 *, normally it is (2+3) * 4


        # 2 3 4 * +  =    3 * 4 + 2

        # 2 3 + 4 * 

        # you can represent reversec polish notation in a stack

from collections import deque
from inspect import stack


def RPL(rplStr):
    stack = []
    rplArr = rplStr.split(" ")
    for i in range (len(rplArr)):
        if (rplArr[i] == "+" or rplArr[i] == "-" or rplArr[i] == "/" or rplArr[i] == "*"):
            operator = rplArr[i]
            operand2 = stack.pop()
            operand1 = stack.pop()
            if (operator == "+"):
                stack.append(operand1+operand2)
            elif (operator == "-"):
                stack.append(operand1 - operand2)
            elif (operator == "/"):
                stack.append(operand1/operand2)
            elif(operator == "*"):
                stack.append(operand1*operand2)
        else:
            stack.append(int(rplArr[i]))
    return stack.pop()

print(RPL("2 3 4 * +"))

    # converting infix to postfix (rpl) expression

def inToPost (rplStr):
    stack = []
    rplArr = rplStr.split(" ")
    outputStr   = ""
    for i in range (len(rplArr)):
        if (rplArr[i] == "+" or rplArr[i] == "-" or rplArr[i] == "/" or rplArr[i] == "*"):
            operator = rplArr[i]
            if (len(stack) == 0):
                stack.append(operator)
            else:
                while (len(stack) != 0 and precedence(rplArr)):
                    outputStr += stack.pop() + " "
                
                stack.append(operator)
        else:
            outputStr += rplArr[i] + " "
        print(stack,outputStr)
    while (len(stack)!= 0):
        outputStr += stack.pop() + " "
    return outputStr

def precedence (topStack, operator):
    return ((operator == "+" or operator == "-") or ((stack[-1] == "*" or stack[-1] == "/") and (operator == "*" or operator == "/")))

# print(inToPost("5 * 10 - 1"))
# print(inToPost("5 * 10 + 1 - 5 * 2"))
# print(inToPost("5 - 1 * 10 - 2 - 5 * 10"))
# print(inToPost("5 / 2 * 5 / 2 + 100000000 - 39 * 3 * 4 / 1"))

# (5 + 3) * (3 - 2) -> 5 3 + 3 2 - *
# (5 + 3) * (3 * 3) -> 5 3 + 3 3 * *


# queue 
# methods: enque and deque
# first in first out FIFO

    # josephus problem - https://courseworks2.columbia.edu/courses/162921/files/folder/Exercises?preview=14720983

def josephus(n,skip):
    queue = []
    for i in range (n):
        queue.append(i)
    while(len(queue) > 1):
        for j in range (skip - 1):
            pop = queue.pop(0)
            queue.append(pop)
        queue.pop(0)
        
    return queue.pop(0)

print(josephus(7,3))




# stacks and queues are just lists in python
# they arent a seperate data structure




