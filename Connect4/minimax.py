# Name: Gaurav Ajariwal
# UTA ID: 1001396273
# Class: CSE 4308

from MaxConnect4Game import *
import copy

def possibleMoves_func(board):
    possibleMoves = []
    for col, colVal in enumerate(board[0]):
        if colVal == 0:
            possibleMoves.append(col)
    return possibleMoves

def result(old_Game, column):
    new_Game = maxConnect4Game()

    try:
        new_Game.nodeDepth = old_Game.nodeDepth + 1
    except AttributeError:
        new_Game.nodeDepth = 1

    new_Game.pieceCount = old_Game.pieceCount
    new_Game.gameBoard = copy.deepcopy(old_Game.gameBoard)
    if not new_Game.gameBoard[0][column]:
        for i in range(5, -1, -1):
            if not new_Game.gameBoard[i][column]:
                new_Game.gameBoard[i][column] = old_Game.currentTurn
                new_Game.pieceCount += 1
                break

    if old_Game.currentTurn == 1:
        new_Game.currentTurn =2
    elif old_Game.currentTurn == 2:
        new_Game.currentTurn = 1


    new_Game.checkPieceCount()
    new_Game.countScore()

    return new_Game


class minimax:
    def __init__(self, game, depth):
        self.currentTurn = game.currentTurn
        self.game = game
        self.maxDepth = int(depth)
    
    def makeDecision(self):
        minVal = []
        possibleMoves = possibleMoves_func(self.game.gameBoard)

        for move in possibleMoves:
            result_move = result(self.game, move)
            minVal.append(self.minVal_func(result_move, 999, -999))

        chosen = possibleMoves[minVal.index(max(minVal))]
        
        return chosen



        #minVal_func for max utility for optimal opponent
    def minVal_func(self, state, alpha, beta):
        if state.pieceCount == 42 or state.nodeDepth == self.maxDepth:
            return self.utility(state)
        v = 999

        for move in possibleMoves_func(state.gameBoard):
            new_State = result(state, move)

            v = min(v, self.maxVal_func(new_State, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)

        return v


    def maxVal_func(self, state, alpha, beta):
        if state.pieceCount == 42 or state.nodeDepth == self.maxDepth:
            return self.utility(state)
        
        v = -999

        for move in possibleMoves_func(state.gameBoard):
            new_State = result(state, move)

            v = max(v, self.minVal_func(new_State, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)

        return v

    
    def utility(self, state):
        if self.currentTurn == 1:
            utility = state.player1Score * 2 - state.player2Score
        elif self.currentTurn == 2:
            utility = state.player2Score * 2 - state.player1Score

        return utility




