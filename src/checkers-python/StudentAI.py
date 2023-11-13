from random import randint
from BoardClasses import Move
from BoardClasses import Board
#The following part should be completed by students.
#Students can modify anything except the class name and exisiting functions and varibles.
class StudentAI():

    def __init__(self,col,row,p):
        self.col = col
        self.row = row
        self.p = p
        self.board = Board(col,row,p)
        self.board.initialize_game()
        self.color = ''
        self.opponent = {1:2,2:1}
        self.color = 2
    def get_move(self, move):
        if len(move) != 0:
            self.board.make_move(move, self.opponent[self.color])
        else:
            self.color = 1

        moves = self.board.get_all_possible_moves(self.color)
        capturing_moves = self.get_capturing_moves(all_moves)
        if capturing_moves:
            selected_move = choice(capturing_moves)
        else:
            index = randint(0,len(moves)-1)
            inner_index =  randint(0,len(moves[index])-1)
            move = moves[index][inner_index]
        self.board.make_move(move,self.color)
        return move
        
    def get_capturing_moves(self, all_moves):
        capturing_moves = []
        for move_group in all_moves:
            for move in move_group:
                if self.is_capturing_move(move):
                    capturing_moves.append(move)
        return capturing_moves

    def is_capturing_move(self, move):
        # Assuming move is a list of tuples (row, col) representing the path of the move
        if len(move) < 2:
            return False

        start_pos = move[0]
        end_pos = move[-1]

        # Check if the move is diagonal and spans two rows and two columns
        if abs(start_pos[0] - end_pos[0]) == 2 and abs(start_pos[1] - end_pos[1]) == 2:
            intermediate_row = (start_pos[0] + end_pos[0]) // 2
            intermediate_col = (start_pos[1] + end_pos[1]) // 2
            intermediate_square = self.board.board[intermediate_row][intermediate_col]

            # Check if the intermediate square has an opponent's piece
            # and the end square is empty (not occupied by any piece)
            return (intermediate_square != None and 
                    intermediate_square.color == self.opponent[self.color] and
                    self.board.board[end_pos[0]][end_pos[1]] == None)

        return False
