sudoku = [
    [0,0,0,1,2,3,0,0,0],
    [0,0,0,0,0,0,7,0,0],
    [0,0,8,0,0,0,0,1,0],
    [0,0,0,0,7,0,5,6,0],
    [0,6,0,0,0,0,0,4,2],
    [0,2,0,0,0,8,0,0,0],
    [4,3,0,0,0,0,0,0,6],
    [0,0,6,0,9,0,8,0,0],
    [0,0,0,0,0,5,0,0,3]
] #0 is for numbers, that we want to solve for 

def pisz(a):  #it's basically some better way to print-out 2d-list
    for i in a:
        print(i)

def test(y,x,n):  #this func tests if given n can be placed in x-th row and y-th collumn
    global sudoku
    for i in range(9):
        if (sudoku[y][i]==n) | (sudoku[i][x]==n):  #checks for any n istances in row and in column
            return False
    y0 = (y//3)*3  #this checks in wich 3x3 sqare (x,y) is
    x0 = (x//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[y0+i][x0+j]==n:  #checks for any n istances in 3x3
                return False
    return True

def do():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0: #if there won't be any 0 places left, do will just pisz()-out the solucion 
                for n in range(1,10):
                    if test(i,j,n):
                        sudoku[i][j]=n
                        do()  #it's basically some backpropagation - program just accepts the first value and checks, if you can solve now = if the value is correct
                        sudoku[i][j]=0
                return
    pisz(sudoku)
    input("Next")
do()
