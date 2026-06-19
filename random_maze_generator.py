#import maze_ui
import numpy as np
import math
import random
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


#region initalising maze
def initalize_maze(numberSquares):
    maze = np.zeros((int(math.sqrt(numberSquares)),int(math.sqrt(numberSquares))),dtype = "int32")
    #initialises the 99 values in the bottom right corner
    maze[int(math.sqrt(numberSquares)-1),int(math.sqrt(numberSquares)-2)] = 1
    
    #initialises the 99 values on the top left corner
    maze[0,1] = 1
    
    inner_maze = generate_inner_maze(numberSquares)
    maze[1:int(math.sqrt(numberSquares)) - 1,1:int(math.sqrt(numberSquares)) - 1] = inner_maze
    #print(maze)
    #generate_maze_object()

    fig, ax = plt.subplots(figsize=(5, 5))
    cmap = mcolors.ListedColormap(["black", "white"])
    ax.imshow(maze, cmap=cmap, vmin=0, vmax=1)
    ax.axis("off")
    plt.tight_layout()

    return fig

#endregion

#region generating maze
def generate_inner_maze(numberSquares):
    valid_maze = np.zeros((int(math.sqrt(numberSquares))-2,int(math.sqrt(numberSquares))-2),dtype = "int32")
    valid_maze[int(math.sqrt(numberSquares)-3),int(math.sqrt(numberSquares)-3)] = 1
    valid_maze[0,0] = 1
    #print(valid_maze)
    starting_node = (0,0)
    target_node = (int(math.sqrt(numberSquares)-3),int(math.sqrt(numberSquares)-3))
    current_pos = starting_node

    stack = [current_pos]
    visited = set()

    max_column_row = int(math.sqrt(numberSquares)-3)
    min_column_row = 0

    while current_pos != target_node:

        (row,col) = current_pos
        #neighbours are in the order of up, down, left, right
        neighbours_changes = [(-1,0),(1,0),(0,1),(0,-1)]
        valid_neighbours = []

        for i,j in neighbours_changes:
            new_row = row + i
            new_col = col + j
            if (new_row <= max_column_row and new_row >= min_column_row) and (new_col <= max_column_row and new_col >= min_column_row):
                new_pos = (new_row,new_col)
                if new_pos not in visited:
                    valid_neighbours.append(new_pos)

        #using random to work out the next "node" in the path using the random module
        if len(valid_neighbours)!=0:
            next_position = random.choice(valid_neighbours)

            #adds the current pos to the visited set
            visited.add(current_pos)
            stack.append(current_pos)
            #changes the position of the current pos to the next pos
            current_pos = next_position
            row,col = current_pos
            valid_maze[row,col] = 1
        else:
            stack.pop()
            if stack:
                current_pos = stack[-1]
    #stack is outputted in the order of the inner maze instead of the full maze
    #print(stack)
    return valid_maze
#endregion


