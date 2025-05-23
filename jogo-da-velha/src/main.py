from gui import GameGUI
from game import Game

def main():
    game = Game()
    gui = GameGUI(game)
    gui.run()
#     main()
if __name__ == "__main__":
    main()