board=[
    ['r','n','b','q','k','b','n','r'],
    ['p','p','p','p','p','p','p','p'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['.','.','.','.','.','.','.','.'],
    ['P','P','P','P','P','P','P','P'],
    ['R','N','B','Q','K','B','N','R']
]






for row in board:
    for col in row:
        print(col, end='  ')
    print("\n")



x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

temp = board[x2][y2]
board[x2][y2] = board[x1][y1]
board[x1][y1] = temp


for row in board:
    for col in row:
        print(col, end='  ')
    print("\n")

turn based move :

whiteTurn = True
whiteTurn = not whiteTurn 
