from app import board, ship
from app import move_and_rules as mv

debug = False

def colLetterToIndex(letter: str) -> int:
    return ord(letter)-ord('A')

def clearScreen():
    print('\x1b[H\x1b[2J')

def color(char: str) -> str:
    cores = {
        "~": "\033[94m~\033[0m",  # azul (água)
        "X": "\033[91mX\033[0m",  # vermelho (acerto)
        "O": "\033[90mO\033[0m",  # cinza (erro)
        "+": "\033[93m+\033[0m",  # amarelo (navio destruído)
    }
    return cores.get(char, char)

def printBoard(board: list[list[str]]):
    size = len(board)
    letras = [chr(ord('A') + i) for i in range(size)]
    print("    " + "  ".join(letras))
    for i, linha in enumerate(board):
        num_linha = str(i + 1).rjust(2)
        linha_colorida = [color(c) for c in linha]  # visual apenas!
        print(f"{num_linha}  " + "  ".join(linha_colorida))

def printRealBoard(real_board: list[list[str]]):
    print("\n\033[95m[ TABULEIRO REAL - DEBUG ]\033[0m")
    size = len(real_board)
    letras = [chr(ord('A') + i) for i in range(size)]
    print("    " + "  ".join(letras))
    for i, linha in enumerate(real_board):
        num_linha = str(i + 1).rjust(2)
        print(f"{num_linha}  " + "  ".join(linha))

def printGameOver():
    clearScreen()
    print("\033[91m")
    print("╔════════════════════════════════════╗")
    print("║                                    ║")
    print("║              GAME OVER             ║")
    print("║                                    ║")
    print("╚════════════════════════════════════╝")
    print("\033[0m")

def printVictory():
    clearScreen()
    print("\033[92m")
    print("╔════════════════════════════════════╗")
    print("║                                    ║")
    print("║           VOCÊ VENCEU!             ║")
    print("║  Todos os navios foram afundados!  ║")
    print("║                                    ║")
    print("╚════════════════════════════════════╝")
    print("\033[0m")

def askRetry() -> bool:
    while True:
        print("\nDeseja jogar novamente? (s/n)")
        op = input("> ").strip().lower()
        if op in ('s', 'sim'):
            return True
        elif op in ('n', 'nao', 'não'):
            return False
        else:
            print("\033[93mDigite 's' para sim ou 'n' para não.\033[0m")

def difficulty():
    cond = False
    escolha = 0
    while not cond:
        print("\033[96m╔════════════════════════════════╗")
        print("║      ESCOLHA A DIFICULDADE     ║")
        print("╠════════════════════════════════╣")
        print("║  1. Fácil    (50 Tentativas)   ║")
        print("║  2. Médio    (42 Tentativas)   ║")
        print("║  3. Difícil  (35 Tentativas)   ║")
        print("╚════════════════════════════════╝\033[0m")
        print("Digite uma opção (1-3)")
        escolha = input(">").strip()
        if escolha == 'zerod': #debug
            global debug
            debug = True
            return 0
        if not escolha.isnumeric() or (int(escolha) > 3 or int(escolha) < 1):
            print('\033[91mEscolha um número entre 1 e 3!\033[0m')
        else:
            cond = True
    return int(escolha)

def inputCoord(board_size: int) -> tuple[int, int]:
    while True:
        coord = input('\nDigite a coordenada (ex: A5): ').strip().upper()

        if len(coord) < 2 or not coord[0].isalpha() or not coord[1:].isdigit():
            print("\033[91mFormato inválido. Use algo como A5.\033[0m\x1B[2A")
            continue

        x = colLetterToIndex(coord[0])
        y = int(coord[1:]) - 1

        if x < 0 or x >= board_size or y < 0 or y >= board_size:
            print(f"\033[91mCoordenada fora do tabuleiro. Use A1 até {chr(ord('A')+board_size-1)}{board_size}.\033[0m\x1B[2A")
            continue

        return x, y

def mainLoop(visible_board: list[list], board_size: int, ships: list[dict], ships_board: list[list], attemps: int) -> bool:
    destroyeds = 0
    while attemps > 0:
        clearScreen()
        printBoard(visible_board)
        if debug:
            printRealBoard(ships_board) 
            [print(s) for s in ships]

        print('\x1b[s', end='')
        print(f'\x1b[3;{board_size*4}H\x1b[32mTentativas restantes: {attemps}\x1b[0m', end='')
        print('\x1b[u', end='')
        
        x, y = inputCoord(board_size)
        while not mv.bomb(x, y, visible_board, ships_board):
            print("\033[91mEssa posição é repetida.\033[0m\x1B[2A")
            x, y = inputCoord(board_size)

        ship.updateShips(ships, visible_board)
        board.updateBoard(visible_board, ships)

        destroyeds = mv.destroyedShips(ships)
        print(f'\x1b[5;{board_size*4}H\x1b[32mNavios destruidos: {destroyeds}\x1b[0m', end='')
        print('\x1b[u', end='')
        attemps -= 1

        if mv.isVictory(ships):
            return True
    return False
    