from ast import And
from connect4 import Connect4

class GameTree:
    #Values: -1 = o loses 0 = tie 1 = o wins
    def __init__(self, connect):
        self.connect = connect.copy()
        self.children = []

    def value(self):
        if self.connect.check_game_over():
            if self.connect.wins == None:
                return 0
            elif self.connect.wins == 'o' and self.connect.who_moves == 'x':
                return 1
            else:
                return -1

        possibilities = self.connect.possible_drops()
        for move in possibilities:
            connectCopy = self.connect.copy()
            connectCopy.drop_token(move)
            child = GameTree(connectCopy)
            self.children.append(child.value())
        if self.connect.who_moves == 'x':
            return min(self.children)
        else:
            return max(self.children)


