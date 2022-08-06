# graphs 
# vertices and edges

# directed = one way
# undirected = both ways

# there can be weight on the edges 
# ex. how much it costs to travel to one node 


# path - sequence of vertices between two vertices
# sich that there is an edge between each vertices


# connectedness 
# a graph is connected if there is some path between
# any pair of verties

# directed graphs: weak and strong connectivity
# weak: if you ignore the direction, it is connected
# strong: considering the direction, you are still able to reach any node


# a graph contains a cycle if you can get back from the vertex you are on

# directed acyclic (DAG) - a directed graph without cycles


# Graph Algorritism

# Topological Sort (Directed Acyclic)
    # if there is a path between s and t in the graph, then S must 
    # appear before t in the topoligical sort

    # Step 1: comput the in degree (number of edges that point to the vertex) of each v ertex
    # Step 2: use a queue and enqueue all vertices with in-degree 0 
    # while the queeu is not empty, get the next vertex s , add s to the ouput
    # for all neighbors of s, t.indegree -= 1
    # if t.indegree ==0, enqueue t

# Graph Implementation


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
    