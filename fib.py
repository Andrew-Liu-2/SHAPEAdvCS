def bfs(graph,source):
    discovered = set()
    queue = []
    queue.append(source)
    discovered.add(source)

    while len(queue) is not 0:
        print(queue)
        value = queue.pop(0)
        print(value)
        for element in graph[value]:
            if element not in discovered:
                discovered.add(value)
                queue.append(value)




    

g = \
{'A': ['B','C'],
 'B': ['A','D','C'],
 'C': ['A','B','D','E'], 
 'D': ['B','C','E','F'],
 'E': ['C','D','F'],
 'F': ['D','E']}

(bfs(g,'A'))