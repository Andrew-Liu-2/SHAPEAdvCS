"""
SHAPE Summer 2022

In this assignment you will implement and compare different search strategies
for solving the n-Puzzle, which is a generalization of the 8 and 15 puzzle to
squares of arbitrary size (we will only test it with 8-puzzles for now). 
See Courseworks for detailed instructions.
"""

import time

def state_to_string(state):
    row_strings = [" ".join([str(cell) for cell in row]) for row in state]
    return "\n".join(row_strings)


def swap_cells(state, i1, j1, i2, j2):
    """
    Returns a new state with the cells (i1,j1) and (i2,j2) swapped. 
    """
    value1 = state[i1][j1]
    value2 = state[i2][j2]
    
    new_state = []
    for row in range(len(state)): 
        new_row = []
        for column in range(len(state[row])): 
            if row == i1 and column == j1: 
                new_row.append(value2)
            elif row == i2 and column == j2:
                new_row.append(value1)
            else: 
                new_row.append(state[row][column])
        new_state.append(tuple(new_row))
    return tuple(new_state)
    

def get_successors(state):
    """
    This function returns a list of possible successor states resulting
    from applicable actions. 
    The result should be a list containing (Action, state) tuples. 
    For example [("Up", ((1, 4, 2),(0, 5, 8),(3, 6, 7))), 
                 ("Left",((4, 0, 2),(1, 5, 8),(3, 6, 7)))] 
    """ 
    child_states = []

    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == 0:
                if column < len(state)-1: # Left 
                    new_state = swap_cells(state, row,column, row, column+1)
                    child_states.append(("Left",new_state))
                if column > 0: # Right 
                    new_state = swap_cells(state, row,column, row, column-1)
                    child_states.append(("Right",new_state))
                if row < len(state)-1:   #Up 
                    new_state = swap_cells(state, row,column, row+1, column)
                    child_states.append(("Up",new_state))
                if row > 0: # Down
                    new_state = swap_cells(state, row,column, row-1, column)
                    child_states.append(("Down", new_state))
                break
    return child_states

            
def goal_test(state):
    """
    Returns True if the state is a goal state, False otherwise. 
    """    
    counter = 0
    for row in state:
        for cell in row: 
            if counter != cell: 
                return False 
            counter += 1
    return True
   
def bfs(state):
    """
    Breadth first search.
    Returns A list of actions
    Should print:  the number of states expanded, and the maximum size of the frontier.  
    """
    original_state = state

    discovered = set()
    queue = []
    queue.append(state)
    discovered.add(state)
    total_visited_states = 0

    prev = {}
    actions = {} # for each discovered state,
                 # what is the action that 
                 # took you there

    # Write code here for bfs.  
    
    while (queue):
        # print(queue)
        currState = queue.pop(0)
        for tuples in get_successors(currState):
            nextAction = tuples[0]
            nextState = tuples[1]
            if nextState not in discovered:
                
                discovered.add(nextState)
                queue.append(nextState)
                total_visited_states +=1
                prev[nextState] = currState
                actions[nextState] = nextAction
                total_visited_states += 1
                if(goal_test(nextState)):
                    # aciton that took the state to the solution state
                    currentState= nextState
                    previousState = prev[currentState]
                    previousAction = actions[currentState]

                    returnActionLi = [previousAction]
                    returnStatesLi = [previousState]
                    while(currentState != original_state):
                        previousState = prev.get(currentState)
                        previousAction = actions.get(previousState)
                        returnActionLi = [previousAction] + returnActionLi
                        returnStatesLi = [previousState] + returnStatesLi
                        currentState = previousState
                    # extra action at the begginning
                    returnActionLi = returnActionLi[1:len(returnActionLi)]
                    print(returnActionLi)
                    print("Total visited states:", total_visited_states)
                    return returnActionLi

                    # need to backtrack to get steps
                    
            

      

    print("Total visited states:", total_visited_states)
    return None# No solution found
                               
     
def dfs(state):
    """
    Breadth first search.
    Returns A list of actions
    Should print:  the number of states expanded, and the maximum size of the frontier.  
    """
    original_state = state

    discovered = set()
    stack = []
    stack.append(state)
    discovered.add(state)
    total_visited_states = 0

    prev = {}
    actions = {} # for each discovered state,
                 # what is the action that 
                 # took you there

    # Write code here for bfs.  
    
    while (stack):
        # print(queue)
        currState = stack.pop()
        for tuples in get_successors(currState):
            nextAction = tuples[0]
            nextState = tuples[1]
            if nextState not in discovered:
                
                discovered.add(nextState)
                stack.append(nextState)
                total_visited_states +=1
                prev[nextState] = currState
                actions[nextState] = nextAction
                if(goal_test(nextState)):
                    # aciton that took the state to the solution state
                    currentState= nextState
                    previousState = prev[currentState]
                    previousAction = actions[currentState]

                    returnActionLi = [previousAction]
                    returnStatesLi = [previousState]
                    while(currentState != original_state):
                        previousState = prev.get(currentState)
                        previousAction = actions.get(previousState)
                        returnActionLi = [previousAction] + returnActionLi
                        returnStatesLi = [previousState] + returnStatesLi
                        currentState = previousState
                    # extra action at the begginning
                    returnActionLi = returnActionLi[1:len(returnActionLi)]
                    print("Total visited states:", total_visited_states)
                    # print(returnActionLi)
                    return returnActionLi

                    # need to backtrack to get steps
                    
            

      

    print("Total visited states:", total_visited_states)
    return None# No solution found


def misplaced_heuristic(state):
    """
    Returns the number of misplaced tiles.
    """
    return 0 # replace this


def manhattan_heuristic(state):
    """
    For each misplaced tile, compute the manhattan distance between the current
    position and the goal position. THen sum all distances. 
    """

    return 0 # replace this


def greedy(state, heuristic = misplaced_heuristic):
    """
    Greedy search is a variant of depth-first search that uses a heuristic to 
    select the next state from the immediate successor states.  
    Returns three values: A list of actions.

    Should print:  the number of states expanded, and the maximum size of the frontier.  
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    from heapq import heappush
    from heapq import heappop

    parents = {}
    actions = {}
    costs = {}

    costs[state] = 0

    # Write best first search here.

    return None # No solution found


def best_first(state, heuristic = misplaced_heuristic):
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns: A list of actions
    Shoudl print: the number of states visited, and the maximum size of the frontier.  
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    from heapq import heappush
    from heapq import heappop

    parents = {}
    actions = {}
    costs = {}

    costs[state] = 0

    # Write best first search here.

    return None # No solution found


def astar(state, heuristic = misplaced_heuristic):
    """
    A-star search using the heuristic function passed as a parameter. 
    Returns: A list of actions
    Should print: the number of states expanded, and the maximum size of the frontier.  
    """
    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here

    from heapq import heappush
    from heapq import heappop

    parents = {}
    actions = {}
    costs = {}

    costs[state] = 0
    
    # Write A* search here

    return None # No solution found


def print_result(solution):
    """
    Helper function to format test output. 
    """
    if solution is None: 
        print("No solution found.")
    else: 
        print("Solution has {} actions.".format(len(solution)))



if __name__ == "__main__":

    
    # Easy test case
    test_state = ((1, 4, 2),
                  (0, 5, 8), 
                  (3, 6, 7))  
     
    

    # More difficult test case
    # test_state = ((7, 2, 4),
    #              (5, 0, 6), 
    #              (8, 3, 1))  
    

    print(state_to_string(test_state))
    print()

    print("====BFS====")
    start = time.time()
    solution = bfs(test_state) #
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))

    print() 
    print("====DFS====") 
    start = time.time()
    solution = dfs(test_state)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))


    print("====Greedy====") 
    start = time.time()
    solution = greedy(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    

    print() 
    print("====Best-First====") 
    start = time.time()
    solution = best_first(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    
    print() 
    print("====A*====") 
    start = time.time()
    solution = astar(test_state, misplaced_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))



