from webbrowser import get


def deleteWall (maze, current, neighbor):
  if neighbor[0] == current[0]: # either left or right
    if neighbor[1] == current[1] + 1: # right
      maze[current][2] = 0
      maze[neighbor][0] = 0
      #delete right of curr and left of nighbor
    elif neighbor[1] == current[1] -1 : # left
      maze[current][0] = 0
      maze[neighbor][2] = 0
      # delete left of curr and right of neighbor
  elif neighbor[1] == current[1]: # either top or bottom
    if neighbor[0] == current[0] - 1:
      maze[current][1] = 0
      maze[neighbor][3] = 0
      # delete top of curr and bottom of neighbor
    elif neighbor[0] == current[0] + 1:
      maze[current][3] = 0
      maze[neighbor][1] = 0
      # delete bottom of curr and top of neighbor


def make_empty_maze(width, height, walls = False): 
  maze = {}
  for row in range(height): 
    for column in range(width): 
      if walls: 
        maze[(row, column)] = [1,1,1,1]
      else: 
        maze[(row, column)] = [0,0,0,0]

  return maze
def getAllNeighbors(maze, height,width,y,x):
  neighbors = []
  if y < height - 1:
    if(allWallsIntact(maze,y+1,x)):
      neighbors.append((y+1,x))
  if y > 0: # left
    if(allWallsIntact(maze,y-1,x)):
      neighbors.append((y-1,x))
  if x < width - 1:
    if(allWallsIntact(maze,y,x+1)):
      neighbors.append((y,x+1))
  if x > 0: # top
    if(allWallsIntact(maze,y,x-1)):
      neighbors.append((y,x-1))
  return neighbors
def allWallsIntact(maze,y,x):
  walls = maze[y,x]
  for i in range(4):
    if walls[i] == 0:
      return False
  return True

maze = make_empty_maze(3,3,True)

print(getAllNeighbors(maze,3,3,1,0))
