from games import *

class GameOfNim(Game):
    """Play Game of Nim with first player 'MAX'.
    A state has the player to move, a cached utility, a list of moves in
    the form of a list of (x, y) positions, and a board, in the form of
    a list with number of objects in each row."""

    def __init__(self, board=[7,5,3,1]):
        moves=[]
        for x in range(0,len(board)):
            for y in range(1,board[x]+1):
                moves.append((x,y))
        self.initial = GameState(to_move="MAX", utility=0,board=board, moves=moves)

    def actions(self, state):
        """Legal moves are at least one object, all from the same row."""
        return state.moves

    def result(self, state, move):
            board1=state.board
            valid_moves=[]
            possible_moves=[]
            for x in range(0,len(board1)):
                for y in range(1,board1[x]+1):
                    possible_moves.append((x,y))

            if move in possible_moves and move[1]<=board1[move[0]]:
                board1[move[0]]=board1[move[0]]-move[1]
                for x in range(0,len(board1)):
                    for y in range(1,board1[x]+1):
                        valid_moves.append((x,y))
                        
            return GameState(to_move=('MIN' if state.to_move == 'MAX' else 'MAX'),
                         utility=self.utility(state,state.to_move),board=board1, moves=valid_moves)

    def utility(self, state, player):
        """Return the value to player; 1 for win, -1 for loss, 0 otherwise."""
        if player == 'MAX':
            return 1
        elif player== 'MIN':
            return -1
        else:
            return 0


    def terminal_test(self, state):
        """A state is terminal if there are no objects left"""
        return state.utility != 0 or len(state.moves) == 0


    def display(self, state):
        board = state.board
        print("board: ", board)
    
    def to_move(self, state):
        return state.to_move

if __name__ == "__main__":
    nim = GameOfNim(board=[0, 5, 3, 1]) # Creating the game instance
    # nim = GameOfNim(board=[7, 5, 3, 1]) # a much larger tree to search
    
    print(nim.initial.board) # must be [0, 5, 3, 1]
    print(nim.initial.moves) # must be [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 1), (2, 2), (2, 3), (3, 1)]
    print(nim.result(nim.initial, (1,3) ))
    utility = nim.play_game(alpha_beta_player, query_player) # computer moves first 
    if (utility < 0):
        print("MIN won the game")
    else:
        print("MAX won the game")
