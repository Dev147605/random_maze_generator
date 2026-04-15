import numpy as np
import math
import maze_ui

numberSquares = maze_ui.numberSquare
maze = np.ones((int(math.sqrt(numberSquares)),int(math.sqrt(numberSquares))),dtype = "int32")
valid_maze = np.zeros((int(math.sqrt(numberSquares))-2,int(math.sqrt(numberSquares))-2),dtype = "int32")

#region initalising maze
def initalize_maze(maze,valid_maze):
    maze[1:int(math.sqrt(numberSquares)-1),1:int(math.sqrt(numberSquares)-1)] = valid_maze
    maze[int(math.sqrt(numberSquares)-1),int(math.sqrt(numberSquares)-2)] = 99
    maze[int(math.sqrt(numberSquares)-2),int(math.sqrt(numberSquares)-2)] = 99
    maze[0,1] = 99
    maze[1,1] = 99
    print(maze)
    generating_maze(valid_maze)
#endregion

def generating_maze(valid_maze):
    starting_node = (0,0)
    target_node = (len(valid_maze)-1,len(valid_maze)-1)
    (current_node) = starting_node
    stack = [starting_node]
    visited = []
    #while stack:
        #right = current_node
        #print(current_node, type(current_node))
    (row,col) = current_node
    neighbours = [(row+1,col),
                    (row-1,col),
                    (row,col+1),
                    (row,col-1)]
    #right left down up
    print(neighbours)



initalize_maze(maze,valid_maze)
