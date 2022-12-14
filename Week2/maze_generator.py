"""
Maze visualizer 

@author: Daniel Bauer 
"""

from tkinter import *
import random
import time

def make_empty_maze(width, height, walls = False): 
  maze = {}
  for row in range(height): 
    for column in range(width): 
      if walls: 
        maze[(row, column)] = [1,1,1,1]
      else: 
        maze[(row, column)] = [0,0,0,0]

  return maze

def make_simple_maze(width, height, n = 10):
  maze = make_empty_maze(width, height)

  obstacles = set()  
  while len(obstacles) < n: 
    i = random.randint(0,height-1)
    j = random.randint(0,width-1)

    if not (i,j) in obstacles: 
      obstacles.add((i,j))
      # make wall 
      maze[(i,j)] = [1,1,1,1]
      if i > 0:
        maze[(i-1, j)][3] = 1
      if i < height-1: 
        maze[(i+1, j)][1] = 1
      if j > 0: 
        maze[(i, j-1)][2] = 1
      if j < width-1: 
        maze[(i, j+1)][0] = 1
  return maze


def make_maze(width, height): 
  maze = make_empty_maze(width, height, walls = True)  
  cord = (0,0)
  
  stack = []

  visitedCells =1 
  while(visitedCells < height * width):
    neighbors = getAllNeighbors(maze,height,width,cord[0],cord[1])

    if (len(neighbors)> 0):
      randIndex = random.randint(0,len(neighbors) -1)
      nextCord = neighbors[randIndex]
      deleteWall(maze,cord,nextCord)
      stack.append(cord)
      cord = nextCord
      visitedCells+=1
    else:
      cord = stack.pop()
  return maze


def get_neighbors(maze,height,width,y, x):
    neighbors = []
    if x > 0 and maze[(y,x)][0]==0: 
      neighbors.append((y,x-1))
    if y > 0 and maze[(y,x)][1]==0:
      neighbors.append((y-1,x))
    if x < width-1 and maze[(y,x)][2]==0:
      neighbors.append((y,x+1))
    if y < height-1 and maze[(y,x)][3]==0:
      neighbors.append((y+1,x))
    return neighbors

def getAllNeighbors(maze, height,width,y,x):
  neighbors = []
  if y < height - 1: # bottom
    if(allWallsIntact(maze,y+1,x)):
      neighbors.append((y+1,x))
  if y > 0: # top
    if(allWallsIntact(maze,y-1,x)):
      neighbors.append((y-1,x))
  if x < width - 1: # right
    if(allWallsIntact(maze,y,x+1)):
      neighbors.append((y,x+1))
  if x > 0: # left
    if(allWallsIntact(maze,y,x-1)):
      neighbors.append((y,x-1))
  return neighbors
  
def allWallsIntact(maze,y,x):
  walls = maze[y,x]
  for i in range(4):
    if walls[i] == 0:
      return False
  return True

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


class MazeVisualizer(object):

    def __init__(self): 

      self.offset = 0 
      self.cell_size = 10
      self.height = 100
      self.width = 100

      root = Tk()
      root.wm_title("Maze simulator")
      root.lift()
      root.attributes("-topmost", True)
      self.root = root
      self.canvas = Canvas(root,height = self.cell_size * self.height, width = self.cell_size * self.width, borderwidth=0, highlightthickness=0)
      self.canvas.pack()

    def draw_grid(self):
      for i in range(self.height):
        for j in range(self.width):
          self.canvas.create_rectangle(j*self.cell_size, i*self.cell_size, (j+1)*self.cell_size, (i+1)*self.cell_size, outline="gray", fill="white") 
      

    def draw_maze(self, maze):
      self.canvas.create_rectangle(0,0,self.width * self.cell_size-1, self.height * self.cell_size-1, outline="black") # outline

      for i in range(self.height): 
        for j in range(self.width): 
          cell = maze[(i,j)]
          if cell[0]: self.canvas.create_line(j*self.cell_size, i*self.cell_size, j*self.cell_size, (i+1)*self.cell_size, width=2)    # left
          if cell[1]: self.canvas.create_line(j*self.cell_size, i*self.cell_size, (j+1)*self.cell_size, i*self.cell_size, width=2)    # up 
          if cell[2]: self.canvas.create_line((j+1)*self.cell_size, i*self.cell_size, (j+1)*self.cell_size, (i+1)*self.cell_size, width=2)    # right  
          if cell[3]: self.canvas.create_line(j*self.cell_size, (i+1)*self.cell_size, (j+1)*self.cell_size, (i+1)*self.cell_size, width=2)    # down

     
    def bfs_step(self, maze,goal):
      if self.queue:
        u = self.queue.pop(0)
        if not u in self.visited: 

          self.paint_cell(u[0], u[1], "gray")
          self.visited.add(u)
          discovered_now = set()
          for v in get_neighbors(maze, self.height,self.width, u[0], u[1]):
            discovered_now.add(v)
            if not v in self.discovered:
              self.prev[v] = u
              self.discovered.add(v)
              self.queue.append(v) 
              if v == goal: 
                # Draw path
                self.draw_path(goal)
                return

          self.paint_set(self.queue, "green")
          self.root.after(50, lambda: self.bfs_step(maze,goal))
          

    def bfs_visualizer(self, maze, start, goal):
      self.prev = {}
      self.draw_maze(maze)
        
      self.paint_cell(start[0], start[1], "red")
      self.paint_cell(goal[0], goal[1], "black")

      self.queue = [start]
      self.discovered = set([start])

      self.visited = set()
      self.root.after(50, lambda: self.bfs_step(maze,goal))

    def draw_path(self, goal): 
      curr = goal
      while curr in self.prev: 
        self.paint_cell(curr[0], curr[1], "blue")
        curr = self.prev[curr]

 

    def dfs_step(self, maze,goal):
      if self.stack:
        u = self.stack.pop()
        if not u in self.visited: 

          self.paint_cell(u[0], u[1], "gray")
          self.visited.add(u)
          neighbors = get_neighbors(maze, self.height,self.width, u[0], u[1])
          random.shuffle(neighbors)
          for v in neighbors: 
            if not v in self.discovered:
              self.prev[v] = u
              self.paint_cell(v[0], v[1], "green")
              self.discovered.add(v)
              self.stack.append(v) 
              if v == goal: 
                self.draw_path(goal) 
                return

          self.root.after(50, lambda: self.dfs_step(maze,goal))
          
    def dfs_visualizer(self, maze, start, goal):
      self.prev = {}
      self.draw_maze(maze)
        
      self.paint_cell(start[0], start[1], "red")
      self.paint_cell(goal[0], goal[1], "black")

      self.stack= [start]
      self.discovered = set([start])

      self.visited = set()
      self.root.after(50, lambda: self.dfs_step(maze,goal))
  
    def paint_cell(self,y,x, color): 
      self.canvas.create_oval(self.cell_size * x+3, self.cell_size * y+3, self.cell_size* (x+1)-3, self.cell_size * (y+1)-3, fill=color, outline=color)
      
    def paint_set(self, coordinate_set, color):
      for (y,x) in coordinate_set: 
        self.paint_cell(y,x, color)

    def run(self):
      #maze = make_simple_maze(self.height, self.width, 80) 
      # maze = make_empty_maze(self.height, self.width, walls = True) 
      maze = make_maze(self.height,self.width)
      self.draw_maze(maze)
      self.bfs_visualizer(maze, (0,0), (self.height-1, self.width-1))
      self.dfs_visualizer(maze, (0,0), (self.height-1, self.width-1))
      self.canvas.mainloop()
 
def main():
    

  gui = MazeVisualizer()
  gui.run()

if __name__ == "__main__":
  main()
    