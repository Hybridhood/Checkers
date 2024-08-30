import pygame

class Board:
    def __init__(self, x_size, y_size, screen):
        self.x_size = x_size
        self.y_size = y_size
        self.screen = screen
        self.brd = self.create_board()
        self.mousepress = False
        self.piece = None

    def create_board(self):
        rows, cols = 8, 8
        board_list = [[0 for _ in range(cols)] for _ in range(rows)]
        for x in range(0, 3):
            for y in range(0, 8):
                if y % 2 != x % 2: 
                    board_list[x][y] = "X"
        for x in range(5, 8):
            for y in range(0, 8):
                if y % 2 != x % 2:
                    board_list[x][y] = "O"
        return board_list
    def get_board(self):
        return self.brd
    def draw_board(self):
        for x in range(len(self.brd)):
            for y in range(len(self.brd)):
                if y % 2 == x % 2:
                    pygame.draw.rect(self.screen, "black", (x * self.x_size, y * self.y_size, self.x_size, self.y_size))
        for x in range(len(self.brd)):
            for y in range(len(self.brd)):
                if self.brd[x][y] == "X":
                    pygame.draw.circle(self.screen, "white", (y * self.x_size + self.x_size / 2, x * self.y_size + self.y_size / 2), 50)
                elif self.brd[x][y] == "O":
                    pygame.draw.circle(self.screen, "black", (y * self.x_size + self.x_size / 2, x * self.y_size + self.y_size / 2), 50)
                elif self.brd[x][y] == ".":
                    pygame.draw.circle(self.screen, "blue", (y * self.x_size + self.x_size / 2, x * self.y_size + self.y_size / 2), 10)

    def move_piece(self,piece):
        self.mousepress = not self.mousepress
        mp = self.mousepress
        #print(piece)
        #print(mp)
        if piece != None:
            if mp == True:
                if self.brd[piece[0]][piece[1]] == "X":
                    self.brd[piece[0]+1][piece[1]-1] = "."
                    self.brd[piece[0]+1][piece[1]+1] = "."
                    #print(self.brd)
                elif piece == "O":
                    pass
    def select_piece(self):
        self.mousepress = not self.mousepress
        x, y = pygame.mouse.get_pos()
        col = x // 125  
        row = y // 125
        square = row, col
        if self.brd[square[0]][square[1]] == "X":

           
            if square != self.piece:
                for i in range(len(self.brd)):
                    for z in range(len(self.brd)):
                        if self.brd[i][z] == ".":
                            self.brd[i][z] = 0
                            self.piece = None
                self.piece = square
                self.brd[self.piece[0]+1][self.piece[1]-1] = "."
                self.brd[self.piece[0]+1][self.piece[1]+1] = "."

        if self.brd[square[0]][square[1]] == 0:
            #print("happs")
            for i in range(len(self.brd)):
                for z in range(len(self.brd)):
                    if self.brd[i][z] == ".":
                        self.brd[i][z] = 0
                        self.piece = None





    def toggle_mouse_press(self):
        self.mousepress = not self.mousepress
        return self.mousepress
            
