'''
Challenge 13: Write a Python function to solve sudoku puzzle

>>> solve_sudoku(puzzle)

puzzle = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
            ]

'''

from itertools import product

def solve_sudoku(puzzle):
    for (row,col) in product(range(0,9), repeat=2):
        if puzzle[row][col] == 0:
            for num in range(1,10):
                allowed = True

                #check in row/column
                for i in range(0,9):
                    if (puzzle[row][i]==num) or (puzzle[i][col]==num):
                        allowed = False
                        break

                #check in box
                r = row - (row % 3)
                c = col - (col % 3)
                for (i,j) in product(range(r,r+3),range(c,c+3)):
                    if puzzle[i][j]==num:
                        allowed = False
                        break

                #if allowed
                if allowed:
                    puzzle[row][col]=num
                    if solve_sudoku(puzzle):
                        return puzzle
                    else:
                        puzzle[row][col] = 0
                    #puzzle[row][col]=0
            return False
    return puzzle
            



def print_puzzle(puzzle):
    for (row,i) in zip(puzzle,range(0,9)):
        for (col,j) in zip(row,range(0,9)):
            if j==3 or j==6:
                print('|',end=' ')
            #else:
            print(col,end=' ')
        print()
        if i==2 or i==5:
            for l in range(0,11):
                print('-',end=' ')
            print()


#-----------------------------------------------------                
            
            
            
puzzle = [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9]
            ]
print('--------Puzzle--------\n')
print_puzzle(puzzle)
print('\n\n-------Solution-------\n')
solution = solve_sudoku(puzzle)

print_puzzle(solution)
