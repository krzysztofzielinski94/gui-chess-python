from os import system
from termcolor import colored
from board import Board

class Game:
    def __init__(self):
        system('cls')
        self.board_game = Board()
        self.turn = 1
        self.winner = ''
        #self.start_game()

    def get_board(self):
        return self.board_game.get_board()

    def upate_board(self, from_move, to_move):
        if self.end_game() != True:
            player = 'W' if self.turn % 2 else 'B'
            enemy_player = 'W' if player == 'B' else 'B'
            self.turn += 1
            self.board_game.show()
            self.board_game.update_piece_position(from_move, to_move, player, enemy_player)
            check = self.board_game.is_check(player, enemy_player)
            if check == True:
                check_mate = self.board_game.is_check_mate(player, enemy_player)
                if check_mate == True:
                    self.winner = enemy_player
        else:
            print ('END GAME!')

    def get_winner(self):
        return self.winner  


    def end_game(self):
        return self.board_game.get_board_status()

if __name__ == '__main__':
    game = Game()