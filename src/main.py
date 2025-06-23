from game import board, ship

tamanho_tabuleiro = 10

navios = [
    ship.createShip("Porta-aviões", 5, letter='P', board_size=tamanho_tabuleiro),
    ship.createShip("Navio de batalha", 4, letter='N', board_size=tamanho_tabuleiro),
    ship.createShip("Cruzador", 3, letter='C', board_size=tamanho_tabuleiro),
    ship.createShip("Destruirdor", 2, letter='D', board_size=tamanho_tabuleiro),
    ship.createShip("Destruirdor", 2, letter='D', board_size=tamanho_tabuleiro),
    ship.createShip("Submarino", 1, letter='S', board_size=tamanho_tabuleiro),
    ship.createShip("Submarino", 1, letter='S', board_size=tamanho_tabuleiro)
]


tabuleiro, tab_navios = board.createBoard(tamanho_tabuleiro, navios)

tabuleiro = board.markBomb(tabuleiro, tab_navios, (2,1))

for y in range(tamanho_tabuleiro):
    print("  ".join(tabuleiro[y]))
print()
for y in range(tamanho_tabuleiro):
    print("  ".join(tab_navios[y]))
print()


