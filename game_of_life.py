class Board:

    def __init__(self, board):
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = []
        for y in range(self.rows): # Deep copy board
            self.board.append([board[y][x] for x in range(self.cols)])

    def value(self, y, x):
        if x < 0 or y < 0:
            return 0
        if y >= self.rows:
            return 0
        if x >= self.cols:
            return 0
        return self.board[y][x]

    def num_live_neighbors(self, y, x):
        neighbors = []
        for offset_y, offset_x in [(0,1),(1,0),(-1,1),(1,1)]:
            neighbors.append(self.value(y+offset_y, x+offset_x))
            neighbors.append(self.value(y-offset_y, x-offset_x))
        return sum(neighbors)

    def print(self):
        for y in range(self.rows):
            for x in range(self.cols):
                if self.value(y,x):
                    print('*', end='')
                else:
                    print('-', end='')
            print('')    
    

def gameOfLife(board):
    board_obj = Board(board)
    board_obj.print()
    for y in range(board_obj.rows):
        for x in range(board_obj.cols):
            num_live_neighbors = board_obj.num_live_neighbors(y,x)
            if board_obj.value(y,x): # Alive
                if num_live_neighbors == 2 or num_live_neighbors == 3:
                    new_value = 1
                else:
                    new_value = 0
            else: # Dead
                if num_live_neighbors == 3:
                    new_value = 1
                else:
                    new_value = 0
            board[y][x] = new_value


board = [
[0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,1,0,1,1,0,0,0],
[0,0,0,0,1,0,1,0,0,0,0],
[0,0,0,0,1,0,0,0,0,0,0],
[0,0,1,0,0,0,0,0,0,0,0],
[1,0,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0],
]
idx = 0

while True:
    gameOfLife(board)
    input("n={}".format(idx))
    idx+=1