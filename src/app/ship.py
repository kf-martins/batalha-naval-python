import random

"""
    Direction: 0 - Horizontal (default), 1 - Vertical
"""

# used_letters = set()
occup_pos = set()

def resetStats():
    occup_pos = set()

def createShip(name: str, size: int, pos: tuple[int, int] = None, direction: int = None, letter: str = None, board_size: int = 10) -> dict:
    """Retorna um dicionario com as informações do naivo"""
    if not letter.isalpha() or letter == 'X':
        raise ValueError("Deve ser uma letra alfabética e diferente de X.")

    if direction is None:
        direction = randomDir()

    if pos is None:
        pos_tentadas = set()
        for _ in range(board_size*board_size): # max de posicoes possiveis
            pos_tentativa = randomPos(size, direction, board_size)
            while pos_tentativa in pos_tentadas:
                pos_tentativa = randomPos(size, direction, board_size)
            pos_tentadas.add(pos_tentativa)
            
            posicoes = getShipPos(pos_tentativa, direction, size)
            if all(p not in occup_pos and 0 <= p[0] < board_size and 0 <= p[1] < board_size for p in posicoes):
                pos = pos_tentativa
                break
        else:
            raise RuntimeError("Não foi possível encontrar posição válida para o navio.")   


    posicoes = getShipPos(pos, direction, size)
    for p in posicoes:
        if p in occup_pos:
            raise ValueError(f'Posição {p} já ocupada por outro navio')
        occup_pos.add(p)

    return {"name": name, "size": size, "pos": pos, 'direction': direction, 'letter': letter, 'destroyed': False}

def getShipPos(pos: tuple[int, int], direction: int, size: int) -> list[tuple[int, int]]:
    """Retorna todas as posições ocupadas por um navio dado a posição inicial, direção e tamanho."""
    x, y = pos
    positions = []
    for i in range(size):
        if direction == 0:
            positions.append((x + i, y))
        else:
            positions.append((x, y + i))
    return positions

def updateShip(ship: dict, board: list[list]):
    if not ship.get('destroyed', False):
        positions = getShipPos(ship['pos'], ship['direction'], ship['size'])
        if all(board[y][x] == 'X' for x, y in positions):
            ship['destroyed'] = True

def updateShips(ships: list[dict], board: list[list]):
    for ship in ships:
        updateShip(ship, board)


def randomPos(size: int, direction: int, board_size: int): 
    """Retorna uma tupla com uma posição x e y aleatória"""
    max_x = board_size - size if direction == 0 else board_size - 1
    max_y = board_size - size if direction == 1 else board_size - 1
    return (random.randint(0, max_x), random.randint(0, max_y))

def randomDir():
    return random.randint(0, 1)
