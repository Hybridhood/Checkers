import pygame

class Board:
    def __init__(self, x_size, y_size, screen):
        self.x_size = x_size
        self.y_size = y_size
        self.screen = screen
        self.brd = self.create_board()
        self.mousepress = False
        self.selected = None

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

        
    def select_piece(self):
        self.mousepress = not self.mousepress
        x, y = pygame.mouse.get_pos()
        col = x // 125  
        row = y // 125
        piece_on = row, col
        
        if self.brd[piece_on[0]][piece_on[1]] == "X":
            if piece_on == self.selected:
                self.clear_possible_moves()
                return
            self.clear_possible_moves()
            self.selected = piece_on
            try:
                if self.selected:
                    if self.selected[0] + 1 < 8:
                        if self.selected[1] - 1 >= 0 and self.brd[self.selected[0]+1][self.selected[1]-1] == 0:
                            self.brd[self.selected[0]+1][self.selected[1]-1] = "."
                        if self.selected[1] - 1 >= 0 and self.brd[self.selected[0]+1][self.selected[1]-1] == "O" and self.brd[self.selected[0]+2][self.selected[1]-2] == 0:
                            self.brd[self.selected[0]+1][self.selected[1]-1] = 0
                            self.brd[self.selected[0]+2][self.selected[1]-2] = "."
                        if self.selected[1] + 1 < 8 and self.brd[self.selected[0]+1][self.selected[1]+1] == 0:
                            self.brd[self.selected[0]+1][self.selected[1]+1] = "."
                        if self.selected[1] - 1 >= 0 and self.brd[self.selected[0]+1][self.selected[1]+1] == "O" and self.brd[self.selected[0]+2][self.selected[1]-2] == 0:
                            self.brd[self.selected[0]+1][self.selected[1]+1] == "O"
                            self.brd[self.selected[0]+2][self.selected[1]+2] = "."
            except IndexError:
                print("Out of range")
        
        elif self.brd[piece_on[0]][piece_on[1]] == "O":
            if piece_on == self.selected:
                self.clear_possible_moves()
                return
            self.clear_possible_moves()
            self.selected = piece_on
            try:
                if self.selected:
                    if self.selected[0] - 1 >= 0:
                        if self.selected[1] - 1 >= 0 and self.brd[self.selected[0]-1][self.selected[1]-1] == 0:
                            self.brd[self.selected[0]-1][self.selected[1]-1] = "."
                        if self.selected[1] + 1 < 8 and self.brd[self.selected[0]-1][self.selected[1]+1] == 0:
                            self.brd[self.selected[0]-1][self.selected[1]+1] = "."
            except IndexError:
                print("Out of range")
        if self.selected != None:
            self.check_for_move(piece_on)

    def clear_possible_moves(self):
        for i in range(len(self.brd)):
            for z in range(len(self.brd)):
                if self.brd[i][z] == ".":
                    self.brd[i][z] = 0
        self.selected = None

    def check_for_move(self, piece_on):
        if self.brd[self.selected[0]][self.selected[1]] == "X":
            if self.brd[piece_on[0]][piece_on[1]] == ".":
                self.move_piece_to(piece_on, "X")
        elif self.brd[self.selected[0]][self.selected[1]] == "O":
            if self.brd[piece_on[0]][piece_on[1]] == ".":
                self.move_piece_to(piece_on, "O")
        elif self.brd[piece_on[0]][piece_on[1]] == 0:
            self.clear_possible_moves()

    def move_piece_to(self, piece_on, piece_type):
        self.brd[self.selected[0]][self.selected[1]] = 0
        self.brd[piece_on[0]][piece_on[1]] = piece_type
        self.clear_possible_moves()
    def toggle_mouse_press(self):
        self.mousepress = not self.mousepress
        return self.mousepress
            