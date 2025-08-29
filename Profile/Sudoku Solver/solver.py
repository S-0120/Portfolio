def solve_sudoku(puzzle):
    
    # Ok so this function returns the end solution. 
    # First we find the space in the puzzle i.e empty(-1) with find_next_empty func. 

    row,col = find_next_empty(puzzle)

    if row is None:            #Means that no empty space in puzzle left and hence it is solved!!
        return True
    
    for guess in range(1,10):               #else we guess the no. and check with is_valid func for right solution
        if is_valid(puzzle,guess,row,col):
            puzzle[row][col] = guess        #if guess is valid then we place it in the box 

            if solve_sudoku(puzzle):        #recursively call the main solve_sudoku func again to restart the process for next empty block
                return True

        puzzle[row][col] = -1               #if our guess is not valid then we backtrack and try a new number for that position
    
    return False                            #if all this doesn't work then the puzzle is unsolvable!!



def find_next_empty(puzzle):
    
    #This func iterates over row and col from 0-8 index and returns r&c if -1(empty) is found. Or else returns None,None if no empty box is found.

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,col
    
    return None,None 


def is_valid(puzzle,guess,row,col):

    #rule check : each row,col and 3*3 box should hold unique no. 1-9

    row_vals = puzzle[row]                #We start with checking row for uniqueness,row_vals holds the list of particular row to check if the no. we've guessed is there in that row or not!!  eg puzzle[1] == [2,5,-1,-1.......8] 
    if guess in row_vals:
        return False                      #If guess is present in row_vals list then its invalid

    col_vals = []                         #Then we check the col, we create an empty list to store the list of col after iterating
    for i in range(9):
        col_vals.append(puzzle[i][col])   #we iterate the puzzle and store the col values in col_vals list
    if guess in cols_vals:                #check for guess in col_vals list 
        return False

    row_start = (row//3) *3               #Now we check the 3*3 box for uniqueness, with this formula we get the major rowBlock we're in (9*9 puzzle have 3 major rows at 3 different major col)
    col_start = (col//3) *3               #To get the major colBlock

    for r in range(row_start, row_start+3):           #Iterating over one box/block of 3*3
        for c in range(col_start,col_start+3):
            if puzzle[r][c] == guess:                 #If guess is not unique in that box then we return false 
                return False
    
    return True                           #Go back to main func with the valid guess