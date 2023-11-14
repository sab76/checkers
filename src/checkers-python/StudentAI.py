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

        # Implement logic to find the move with the longest sequence
        # For now, it's selecting a random move
        if moves:
            longest_move = max(moves, key=lambda group: max(len(m) for m in group))
            chosen_move = max(longest_move, key=len)
            self.board.make_move(chosen_move, self.color)
            return chosen_move

        # Fallback to random move if no other move is found
        index = randint(0, len(moves) - 1)
        inner_index = randint(0, len(moves[index]) - 1)
        move = moves[index][inner_index]
        self.board.make_move(move, self.color)
        return move
        