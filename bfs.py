def bfs(graph,source):
    discovered = set()
    queue = []
    queue.append(source)
    discovered.add(source)

    while len(queue) > 0:
        value = queue.pop(0)
        print(value)
        for element in graph[value]:
            if element not in discovered:
                discovered.add(element)
                queue.append(element)




g = \
{'A': ['B','C'],
 'B': ['A','D','C'],
 'C': ['A','B','D','E'], 
 'D': ['B','C','E','F'],
 'E': ['C','D','F'],
 'F': ['D','E']}



bfs(g,'A')

def unweighted_shortest_path(graph,source):
    discovered = set()
    queue = []
    queue.append(source)
    discovered.add(source)
    cost = {}
    cost[source] = 0

    while len(queue) != 0:
        value = queue.pop(0)
        print(value)
        for element in graph[value]:
            if element not in discovered:
                discovered.add(element)
                queue.append(element)
                cost[element] = cost[value] + 1
    return cost

print(unweighted_shortest_path(g,'A'))


def recovering_bfs_path(graph,source,target):
    discovered = set()
    queue = [] 
    queue.append(source)
    discovered.add(source)
    previous = {}


    while len(queue) > 0:
        value = queue.pop(0)
        print(value)
        for element in graph[value]:
            if element not in discovered:
                discovered.add(element)
                queue.append(element)
                previous[element] = value

    returnli = [target]
    currValue = target
    while(currValue!=source):
        returnli = [previous.get(currValue)] + returnli
        currValue = previous.get(currValue)
    return returnli


print(recovering_bfs_path(g,'A','F'))
    