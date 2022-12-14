import numpy as np
import cshogi as shogi

"""
A9, A8, A7, A6, A5, A4, A3, A2, A1
B9, B8, B7, B6, B5, B4, B3, B2, B1
C9, C8, C7, C6, C5, C4, C3, C2, C1
D9, D8, D7, D6, D5, D4, D3, D2, D1
E9, E8, E7, E6, E5, E4, E3, E2, E1
F9, F8, F7, F6, F5, F4 F3, F2, F1
G9, G8, G7, G6, G5, G4, G3, G2, G1
H9, H8, H7, H6, H5, H4, H3, H2, H1
I9, I8, I7, I6, I5, I4, I3, I2, I1
"""

def col_material(board):
    list_B = [shogi.BPAWN, shogi.BLANCE, shogi.BKNIGHT, shogi.BSILVER, shogi.BGOLD,
              shogi.BBISHOP, shogi.BROOK,
              shogi.BPROM_PAWN, shogi.BPROM_LANCE, shogi.BPROM_KNIGHT, shogi.BPROM_SILVER,
              shogi.BPROM_BISHOP, shogi.BPROM_ROOK]
    list_W = [shogi.WPAWN, shogi.WLANCE, shogi.WKNIGHT, shogi.WSILVER, shogi.WGOLD,
              shogi.WBISHOP, shogi.WROOK,
              shogi.WPROM_PAWN, shogi.WPROM_LANCE, shogi.WPROM_KNIGHT, shogi.WPROM_SILVER,
              shogi.WPROM_BISHOP, shogi.WPROM_ROOK]
    point = [1, 3, 4, 6, 7, 10, 12, 6, 6, 6, 6, 12, 14]
    material = 0
    for i in range(len(list_B)):
        material += (board.pieces.count(list_B[i]) * point[i])
        material -= (board.pieces.count(list_W[i]) * point[i])
    material *= {shogi.BLACK: 1, shogi.WHITE: -1}[board.turn]
    return material

class opening_base:
    def __init__(self):
        self.book = {}
        
        self.squares_B = []
        self.pieces_B = []
        self.points_B = []

        self.hozyo_B = []
        self.hozyo_points_B = []

        self.squares_W = []
        self.pieces_W = []
        self.points_W = []

        self.hozyo_W = []
        self.hozyo_points_W = []

    def Eval(self, board):
        if board.turn == shogi.BLACK:
            squares = self.squares_B
            pieces = self.pieces_B
            points = self.points_B
            hozyo = self.hozyo_B
            hozyo_points = self.hozyo_points_B
            king = shogi.KING
        else:
            squares = self.squares_W
            pieces = self.pieces_W
            points = self.points_W
            hozyo = self.hozyo_W
            hozyo_points = self.hozyo_points_W
            king = shogi.KING
        score = 0
        for i in range(len(squares)):
            if board.piece_type(squares[i]) == pieces[i]:
                score += points[i]
        for i in range(len(hozyo)):
            if board.piece_type(hozyo[i]) == king:
                score += hozyo_points[i]
        return score + col_material(board) * 500

class Anaguma(opening_base):
    def __init__(self):
        super().__init__()
        
        self.squares_B = [shogi.H5, shogi.I1, shogi.H1, shogi.H2, shogi.H3, shogi.H2, shogi.H7]
        self.pieces_B = [shogi.ROOK, shogi.KING, shogi.LANCE, shogi.SILVER, shogi.GOLD, shogi.ROOK, shogi.GOLD]
        self.points_B = [100, 300, 3, 3, 3, -10, 10]
        self.hozyo_B = [shogi.H4, shogi.H3, shogi.H2, shogi.I5,  shogi.H6, shogi.H7, shogi.I6]
        self.hozyo_points_B = [30, 50, 100, -50, -110, -110, -110]

        self.squares_W = [shogi.B5, shogi.A9, shogi.B9, shogi.B8, shogi.B7, shogi.B8, shogi.B3]
        self.pieces_W =  [shogi.ROOK, shogi.KING, shogi.LANCE, shogi.SILVER, shogi.GOLD, shogi.ROOK, shogi.GOLD]
        self.points_W = [100, 300, 3, 3, 3, -10, 10]
        self.hozyo_W = [shogi.B6, shogi.B7, shogi.B8, shogi.A5, shogi.B4, shogi.B3, shogi.A4]
        self.hozyo_points_W = [30, 50, 100, -50, -110, -110, -110]

class Mino(opening_base):
    def __init__(self):
        super().__init__()
        self.squares_B = [shogi.H2, shogi.F1, shogi.H6, shogi.H3, shogi.I4, shogi.H5]
        self.pieces_B = [shogi.KING, shogi.PAWN, shogi.ROOK, shogi.SILVER, shogi.GOLD, shogi.GOLD]
        self.points_B = [300, 10, 100, 5, 50, 30]
        self.hozyo_B = [shogi.H4, shogi.H3]
        self.hozyo_points_B = [60, 70]

        self.squares_W = [shogi.B8, shogi.D9, shogi.B4, shogi.B7, shogi.A6, shogi.B5]
        self.pieces_W =  [shogi.KING, shogi.PAWN, shogi.ROOK, shogi.SILVER, shogi.GOLD, shogi.GOLD]
        self.points_W = [300, 10, 100, 5, 50, 30]
        self.hozyo_W = [shogi.B6, shogi.B7]
        self.hozyo_points_W = [60, 70]

class Muteki(opening_base):
    def __init__(self):
        super().__init__()
        self.squares_B = [shogi.I5, shogi.I6, shogi.I7, shogi.H5, shogi.H4, shogi.H6]
        self.pieces_B = [shogi.KING, shogi.GOLD, shogi.GOLD, shogi.ROOK, shogi.SILVER, shogi.SILVER]
        self.points_B = [100, 50, 50, 90, 50, 50]

        self.squares_W = [shogi.A5, shogi.A6, shogi.A7, shogi.B5, shogi.B4, shogi.B6]
        self.pieces_W = [shogi.KING, shogi.GOLD, shogi.GOLD, shogi.ROOK, shogi.SILVER, shogi.SILVER]
        self.points_W = [100, 50, 50, 90, 50, 50]

opening_dict = {0: Anaguma, 1: Mino, 2: Muteki}

class Opening_AI():
    def __init__(self, opening_number=0):
        global opening_dict
        self.mate_move_num = 7
        self.qsearch_depth = 4
        self.opening = opening_dict[opening_number]()
        
        self.MAX = 1000000
        self.MIN = self.MAX * -1
        self.DRAW_V = 0

        self.eval_nodes = {}
        self.ordering_moves = {}

    def reset(self, sfen):
        self.board = shogi.Board(sfen)
        return

    def eval(self):
        hash_v = self.board.zobrist_hash()
        if hash_v in self.eval_nodes.keys():
            return self.eval_nodes[hash_v]
        score = self.opening.Eval(self.board)
        self.eval_nodes[hash_v] = score
        return score

    def change(self, AB):
        return [-AB[1], -AB[0]]

    def Ordering(self):
        hash_v = self.board.zobrist_hash()
        if hash_v in self.ordering_moves.keys():
            return self.ordering_moves[hash_v]
        if self.my_turn == shogi.BLACK:
            yusen1 = ['5i4h', '4h3h', '3h2h', '2h1i']
            yusen2 = ['2h5h', '1i1h']
            yusen3 = ['4i3h', '3i2h']
        else:
            yusen1 = ['5a6b', '6b7b', '7b8b', '8b9a']
            yusen2 = ['8b5b', '9a9b']
            yusen3 = ['4a3b', '3a2b']
        L_moves = list(self.board.legal_moves)
        output1 = []
        output2 = []
        output3 = []
        output4 = []
        for i in range(len(L_moves)):
            usi_move = shogi.move_to_usi(L_moves[i])
            if usi_move in yusen1:
                output1 += [L_moves[i]]
            elif usi_move in yusen2:
                output2 += [L_moves[i]]
            elif usi_move in yusen3:
                output3 += [L_moves[i]]
            else:
                output4 += [L_moves[i]]
        output = output1 + output2 + output3 + output4
        self.ordering_moves[hash_v] = output
        return output

    def return_take_moves(self):
        L_moves = list(self.board.legal_moves)
        if self.board.is_check():
            return L_moves
        output = []
        for i in range(len(L_moves)):
            if self.board.piece(shogi.move_to(L_moves[i])) != 0:
                output.append(L_moves[i])
        return output

    def qsearch(self, depth, AB):
        if self.board.is_game_over():
            return self.MIN
        N_moves = self.return_take_moves()
        if (depth <= 0 or len(N_moves) == 0) and self.my_turn == self.board.turn:
            return self.eval()
        max_score = self.MIN
        for i in range(len(N_moves)):
            self.board.push(N_moves[i])
            result = self.qsearch(depth - 1, self.change(AB))
            self.board.pop()
            if result == self.MIN:
                return self.MAX
            result = result * -1
            if result >= AB[1] and self.my_turn == self.board.turn:
                return result
            AB[0] = max([AB[0], result])
            max_score = max([max_score, result])
        return max_score
    
    def search(self, depth, AlphaBeta):
        if self.board.is_game_over():
            return self.MIN
        if depth <= 2 and self.my_turn == self.board.turn:
            N_moves = self.Ordering()
        else:
            N_moves = list(self.board.legal_moves)
        max_score = self.MIN
        for i in range(len(N_moves)):
            self.board.push(N_moves[i])
            if depth >= self.max_depth:
                result = self.qsearch(self.qsearch_depth, self.change(AlphaBeta))
            else:
                result = self.search(depth + 1, self.change(AlphaBeta))
            self.board.pop()
            if result == self.MIN:
                return self.MAX
            result = result * -1
            if result >= AlphaBeta[1] and self.my_turn == self.board.turn:
                return result
            AlphaBeta[0] = max([AlphaBeta[0], result])
            max_score = max([max_score, result])
        return max_score

    def main(self, sfen):
        self.reset(sfen)
        self.max_depth = 1
        self.my_turn = self.board.turn
        move = self.board.mate_move(self.mate_move_num)
        move = shogi.move_to_usi(move)
        if move != 'None':
            return move
        AlphaBeta = [self.MIN, self.MAX]
        max_score = self.MIN
        N_moves = self.Ordering()
        for i in range(len(N_moves)):
            self.board.push(N_moves[i])
            result = self.search(1, self.change(AlphaBeta))
            self.board.pop()
            if result == self.MIN:
                bestmove = N_moves[i]
                AlphaBeta[0] = self.MAX
                break
            result = result * -1
            if result >= max_score:
                bestmove = N_moves[i]
                max_score = result
            AlphaBeta[0] = max((result, AlphaBeta[0]))
        return shogi.move_to_usi(bestmove)

def test():
    ai = Opening_AI(opening_number=2)
    board = shogi.Board()
    for i in range(8):
        print('')
        print(i)
        print(board)
        print(board.sfen())
        move = ai.main(board.sfen())
        print(move)
        board.push_usi(move)
        print('')
    return

if __name__ == '__main__':
    ai = Opening_AI()
    test()
