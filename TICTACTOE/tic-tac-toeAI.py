
import math
import random

class Board():

    #we create a constructor first 

    def __init__(self):
        self.board = self.create_board()
        self.current_winner = None
    #create a list of 9 empty spaces, i.e. a list of our rows. 
    @staticmethod
    def create_board():
        return [' ' for _ in range(9)] 
    
    #function for creating the tic tac toe baord. 
    def paint_board(self):
         for i in range(3):
             row = self.board[i*3:(i+1) * 3]
             print('| ' + '| '.join(row) + ' |')
            

    @staticmethod
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
    
        if all([rows == letter for rows in row]): 
            return True
        #for columns, we will use the modulo operator to find the column number.
        col_num = cell % 3 
        col = [self.board[col_num+i*3] for i in range(3)]
        
        if all([cols == letter for cols in col]):
            return True 
            
        #for diagonal cells , also remember that there are two diagonals in a 3x3 tic tac toe board.
        if cell % 2 == 0:


            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            diagonal2 = [self.board[i] for i in [2, 4, 6]]

            if all([diagonal1 == letter]):
                return True
            if all([diagonal2 == letter]):
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
        pass 


class Human(Player):

    def __init__(self, letter):
        super().__init__(letter)
    
    def ask_for_move(self, game):

        valid_move = False 
        move = None 
        move = input("Enter the cell no. where you want to make your move(0-8): ")
        try : 
            move = int(move)
            if move not in game.available_moves():
                raise ValueError
            valid_move = True
        except ValueError:
            print("Invalid move. Choose between (0-8) only.")
        return move 


class AI(Player):
    def __init__(self, letter):
        super().__init__(letter)
    def ask_for_move(self, game):
        move = None
        # first if its the starting move, make a random choice
        if len(game.available_moves()) == 9:
            move = random.choice(game.available_moves()) #chooses any one cell in the board. 
        else : 
            move = self.minimax_algo(game, self.letter)['position']
            
        return move    
    def minimax_algo(self, state, player_letter):
        #could be done recursively as well, will do in the future. 
        max_player = self.letter 
         
        if player_letter == 'X':
            other_player = 'O'
        else :
            other_player = 'X' 

        # first we want to check if the previous move is a winner
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_cells() + 1) if other_player == max_player else -1 * (
                        state.num_empty_cells() + 1)} # here we are returning a position and a score, positive for max player and negative for min player 
        elif not state.empty_cells():
            return {'position': None, 'score': 0}

        if player_letter == max_player:
            best = {'position': None, 'score': -math.inf}  # each score should maximize, so seeting minis infinity as the lowest value 
        else:
            best = {'position': None, 'score': math.inf}  # each score should minimize so setting plus infiinity as the highest value
        for possible_move in state.available_moves():
            state.make_move(possible_move, player_letter)
            sim_score = self.minimax_algo(state, other_player)  # simulate a game after making that move

            # undo move, so that the board is in the same state as before.(for backtracking)
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player_letter == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best
    

def play(tic_tac_toe, player1, player2, print_game = True):
        
        #tic_tac_toe is the object of the class Board. 
        if print_game == True:

            tic_tac_toe.show_nums()

        #letter defined in the Player Class as its variable 

        letter = "X"

        while tic_tac_toe.empty_cells():
            #ask for move for player 1
            if letter == "O":
                move = player2.ask_for_move(tic_tac_toe)
            else:
                #ask for move for player 2
                move = player1.ask_for_move(tic_tac_toe)
            
            if tic_tac_toe.make_move(move,letter):
                if print_game:
                    print("Move made by player ", letter, "at cell no.", move)
                    tic_tac_toe.paint_board()

                if tic_tac_toe.winning_player(move, letter):
                    print("Player ", letter, "wins!")
                    return letter #returning the winning player , exiting the loop
                letter = "O" if letter == "X" else "X"

        if print_game: 
            print("It's a tie!")        

#main portion to run the game       
print("Machine : X , Human : O")
ai = AI("X")
human = Human("O")

board = Board()
play(board,ai,human,print_game = True)