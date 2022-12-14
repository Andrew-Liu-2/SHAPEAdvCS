import math
import random
import sys


class FrozenLake(object):

    def __init__(self, width, height, targets, blocked, holes, start):
        self.initial_state = start 
        self.width = width
        self.height = height
        self.targets = set(targets)
        self.holes = set(holes)
        self.blocked = set(blocked)

        # Parameters for the simulation
        self.gamma = 0.9
        self.success_prob = 0.5
        self.fail_prob = 0.25

    def get_reward(self, state):
        if state in self.holes: 
            return -5.0 
        elif state in self.targets:
            return 1.0
        else: 
            return -0.1

    def print_map(self, policy=None):
        sys.stdout.write(" ")
        for i in range(self.width):
            sys.stdout.write("--")
        sys.stdout.write("\n")
        for j in range(self.height): 
            
            sys.stdout.write("|")
            for i in range(self.width): 
                if (i,j) in self.targets:
                    sys.stdout.write("T ")
                elif (i,j) in self.holes:  
                    sys.stdout.write("O ")
                elif (i,j) in self.blocked: 
                    sys.stdout.write("# ")
                else: 
                    if policy and (i,j) in policy:
                        a = policy[(i,j)]
                        if a=="n":
                            sys.stdout.write("^")
                        elif a=="s":
                            sys.stdout.write("v")
                        elif a=="e":
                            sys.stdout.write(">")
                        elif a=="w":
                            sys.stdout.write("<")
                        sys.stdout.write(" ")
                    elif (i,j)==self.initial_state:
                        sys.stdout.write("* ")
                    else: 
                        sys.stdout.write(". ")
            sys.stdout.write("|")
            sys.stdout.write("\n")
        sys.stdout.write(" ")
        for i in range(self.width):
            sys.stdout.write("--")
        sys.stdout.write("\n")

    def get_transitions(self, state, direction):

        result = []
        x,y = state
        remain_p = 0.0

        if direction=="n": 
            success = (x,y-1)
            fail = [(x+1,y), (x-1,y)]
        elif direction=="s":
            success =  (x,y+1)
            fail = [(x+1,y), (x-1,y)]
        elif direction=="e":
            success = (x+1,y)
            fail= [(x,y-1), (x,y+1)]
        elif direction == "w":
            success = (x-1,y)
            fail= [(x,y-1), (x,y+1)]
          
        if success[0] < 0 or success[0] > self.width-1 or \
           success[1] < 0 or success[1] > self.height-1 or \
           success in self.blocked: 
                remain_p += self.success_prob
        else: 
            result.append((success, self.success_prob))
        
        for i,j in fail:
            if i < 0 or i > self.width-1 or \
               j < 0 or j > self.height-1 or \
               (i,j) in self.blocked: 
                    remain_p += self.fail_prob 
            else: 
                result.append(((i,j), self.fail_prob))
           
        if remain_p > 0.0: 
            result.append(((x,y), remain_p))
        return result

    def get_initial_utility_function(self):
        result = {}
        for x in range(self.width): 
            for y in range(self.height): 
                result[(x,y)] = 0.0
        return result

    #### Your code starts here ###
    
    def move(self, state, direction):
        possibleMoves = self.get_transitions(state,direction)
        coordinates = []
        probabilities = []
        for i in range(len(possibleMoves)):
            coordinates.append(possibleMoves[i][0])
            probabilities.append(possibleMoves[i][1])
        return random.choices(coordinates,probabilities,k=1)[0]

        """
        Return the state that results from going in this direction.
        """
        return None # TODO 
    
    def get_random_policy(self):
        policy = {}
        directions = ['n','e','s','w']
        for x in range (self.width):
            for y in range (self.height):
                policy[(x,y)] = random.choice(directions)
        return policy
        """
        Generate a random policy.
        """
        return None # TODO

    def simple_policy_rollout(self, policy):
        currPos = self.initial_state
        while True:
            currPos = self.move( currPos, policy[currPos])
            if(currPos in self.targets):
                return True
            if (currPos in self.holes):
                return False

        """
        Return True if a random trial with this policy is successful.  
        """
        return False # TODO

    def evaluate_policy(self, policy, t=100):
        success = 0
        failure = 0
        for i in range (t):
            if(self.simple_policy_rollout(policy)):
                success +=1
            else:
                failure += 1
        return success/(success + failure)
        """
        Return the percentage of successful trials within t random trials with
        this policy.
        """
        return 0.0 # TODO
    
    def value_iteration(self, epsilon = 0.001):

        def expectedValue(self,currState,action,prevUtilx,y):
            transitions = self.get_transitions((x,y),action)


        util = self.get_initial_utility_function()
        new_util = self.get_initial_utility_function()

        terminated = False
        while not terminated:

            terminated = True
            for x in range(self.width): 
                for y in range(self.height): 
                    value = util[(x,y)]
                    newValue = new_util[(x,y)]
                    
                    
                    value = newValue
                    allActions = ['n','e','s','w']
                    maxValue = 0

                    for action in allActions:
                        transitions = self.get_transitions((x,y),action)
                        value = 0
                        for transition in transitions:
                            value += (util[transition[0]] * transition[1])
                        if(value > maxValue):
                            maxValue = value
                    newValue = self.get_reward((x,y)) + maxValue
                    new_util[x,y] = newValue

                    if(abs(newValue - value) > (epsilon * ((1-self.gamma) / self.gamma))):
                        print(abs(newValue - value),(epsilon * ((1-self.gamma) / self.gamma)))
                        terminated = False
            util = new_util 
        return util
        """
        The value iteration algorithm to iteratively compute an optimal
        utility function.
        """
        return {} # TODO

    def extract_policy(self, utility_function):
        """
        Given a utility function, return the best policy.4 
        """
        return {} # 


if __name__ == "__main__":
   
    # Create a lake simulation 
    lake = FrozenLake(width=8,height=8, targets=[(3,4)], blocked = [(3,3),(2,3),(2,4), ], holes=[(4,0),(4,1),(3,0),(3,1), (6,4),(6,5),(0,7),(0,6),(1,7)], start=(0,0))
    policy = lake.get_random_policy()
    # print(lake.evaluate_policy(policy))
    print(lake.value_iteration(0.001))
    lake.print_map(policy)
    

    
