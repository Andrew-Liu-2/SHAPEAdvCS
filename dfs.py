def dfs(graph,source):
    discovered = set()
    queue = []
    queue.append(source)
    discovered.add(source)

    while len(queue) > 0:
        value = queue.pop()
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

n= \
{
'1' : ['2','3'],
'2' : ['5','6'],
'3' : ['4'],
'4' : [],
'5' : [],
'6' : ['7'],
'7' : []
}


# dfs(n,'1')


def unweighted_shortest_dfs_path(graph,source):
    discovered = set()
    queue = []
    queue.append(source)
    discovered.add(source)
    cost = {}
    cost[source] = 0

    while len(queue) > 0:
        value = queue.pop()
        print(value)
        for element in graph[value]:
            if element not in discovered:
                discovered.add(element)
                queue.append(element)
                cost[element] = cost[value] + 1
    return cost

print(unweighted_shortest_dfs_path(n,'1'))