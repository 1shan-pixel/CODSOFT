
import math
import random

class Board():

    #we create a constructor first 

    def __init__(self):
        self.board = self.create_board()
    #create a list of 9 empty spaces, i.e. a list of our rows. 
    def create_board():
        return [' ' for _ in range(9)] 
    #function for creating the tic tac toe baord. 
    def paint_board(self):
         for i in range(3):
             row = self.board[i*3:(i+1) * 3]
             print('| ' + ' | '.join(row) + ' |')
    
    def show_nums():
        numbers = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)] #a way to create 2 d list in python , creates a list of row nums
        for num in numbers: 
            print('|' + '|'.join(num) + '|') #first memebers of list will be [1,2,3] and so on.

    def winning_player(self,cell,letter):
    #is determined if a player's letter has covered entire row, column or diagonal.
        row_num = math.floor(cell/3)
        row = self.board[row_num*3:(row_num+1)*3]
         #once again creating the empty list of rows
        
       #checking if all the elements in the row are equal to the letter of the player.
        for rows in row: 
            if all(rows == letter ): 
                return True
        #for columns, we will use the modulo operator to find the column number.
        col_num = cell % 3 
        col = [self.board[col_num+i*3] for i in range(3)]
        for cols in col: 
            if all(cols == letter):
                return True 
            
        #for diagonal cells , also remember that there are two diagonals in a 3x3 tic tac toe board.
        if cell % 2 == 0: 

            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all(diagonal1 == letter):
                return True
            if all(diagonal2 == letter):
                return True 
        return False
    
    def available_moves(self):
        moves = []
        for i, s in enumerate(self.board):
            if s == " ":
                moves.append(i)
        return moves

    def empty_cells(self):
        return True if " " in self.board else False
    def num_empty_cells(self):
        return self.board.count(" ")
    
    def play(tic_tac_toe, player1, player2, print_game = True):

        tic_tac_toe.show_nums()
        #letter defined in the Player Class as its variable 

        letter = "X"

        while tic_tac_toe.empty_cells():
            #ask for move for player 1
            if letter == "X":
                move = player1.ask_for_move(tic_tac_toe)
            else:
                #ask for move for player 2
                move = player2.ask_for_move(tic_tac_toe)
            
    #helps to make move on the board based on whether the cell is empty or not. 
    def make_move(self, cell, letter):
        if self.board[cell] == " ":
            self.board[cell] = letter
            #winning player return 
            return True 
        return False


        
class Player():

    def __init__(self, letter):
        self.letter = letter
    def ask_for_move(self, game):

    
class Human(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def ask_for_move(self, game):
        pass
        

class AI(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def ask_for_move(self, game):
        # first if its the starting move, make a random choice
        if len(game.available_moves()) == 9:
            move = random.choice(game.available_moves()) #chooses any one cell in the board. 
    def minimax_algo(self, game, letter):
        pass

