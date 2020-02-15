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
]

def pisz(a):
    for i in a:
        print(i)

def test(y,x,n):
    global sudoku
    for i in range(9):
        if (sudoku[y][i]==n) | (sudoku[i][x]==n):
            return False
    y0 = (y//3)*3
    x0 = (x//3)*3
    for i in range(3):
        for j in range(3):
            if sudoku[y0+i][x0+j]==n:
                return False
    return True

def doo():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j]==0:
                for n in range(1,10):
                    if test(i,j,n):
                        sudoku[i][j]=n
                        doo()
                        sudoku[i][j]=0
                return
    pisz(sudoku)
    input("Next")
doo()
