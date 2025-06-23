from src import game

if __name__ == '__main__':
    
    running = True
    while running:
        debug = False
        tamanho_tabuleiro = 10

        navios = [
            game.ship.createShip("Porta-aviões", 5, letter='P', board_size=tamanho_tabuleiro),
            game.ship.createShip("Navio de batalha", 4, letter='N', board_size=tamanho_tabuleiro),
            game.ship.createShip("Cruzador", 3, letter='C', board_size=tamanho_tabuleiro),
            game.ship.createShip("Destruirdor", 2, letter='D', board_size=tamanho_tabuleiro),
            game.ship.createShip("Destruirdor", 2, letter='D', board_size=tamanho_tabuleiro),
            game.ship.createShip("Submarino", 1, letter='S', board_size=tamanho_tabuleiro),
            game.ship.createShip("Submarino", 1, letter='S', board_size=tamanho_tabuleiro)
        ]

        tabuleiro, tab_navios = game.board.createBoard(tamanho_tabuleiro, navios)

        game.clearScreen()
        tentativas = game.mv.defineDifficulty(game.difficulty())
        win = game.mainLoop(tabuleiro, tamanho_tabuleiro, navios, tab_navios, tentativas)

        if win:
            game.printVictory()
        else:
            game.printGameOver()

        running = game.askRetry()