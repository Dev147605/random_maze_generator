import numpy as np
import math
import maze_ui

numberSquares = maze_ui.numberSquare
print(numberSquares)
maze = np.ones((int(math.sqrt(numberSquares)),int(math.sqrt(numberSquares))),dtype = "int32")
secondary_maze = np.zeros((int(math.sqrt(numberSquares))-2,int(math.sqrt(numberSquares))-2),dtype = "int32")

#region initalising maze
def initalize_maze(maze,secondary_maze):
    maze[1:int(math.sqrt(numberSquares)-1),1:int(math.sqrt(numberSquares)-1)] = secondary_maze
    maze[int(math.sqrt(numberSquares)-1),int(math.sqrt(numberSquares)-2)] = 99
    maze[int(math.sqrt(numberSquares)-2),int(math.sqrt(numberSquares)-2)] = 99
    maze[0,1] = 99
    maze[1,1] = 99
    
    print(maze)
#endregion

#initalize_maze(maze,secondary_maze)
