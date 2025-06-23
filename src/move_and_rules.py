difficulties = {
    '0': 7, #debug
    '1': 50,
    '2': 42,
    '3': 35
}

def defineDifficulty(difficulty: int) -> int:
    return difficulties[str(difficulty)]

def verifyAttemps(attemps: int) -> bool:
    if attemps == 0:
        return False
    return True

def bomb(x, y, visible_board: list[list], ships_board: list[list]) -> bool:
    if visible_board[y][x] != '~':
        return False
    if ships_board[y][x] == '~':
        visible_board[y][x] = 'O'
    else:
        visible_board[y][x] = 'X'
    return True

def destroyedShips(ships: list[dict]) -> int:
    return sum([1 for s in ships if s.get('destroyed')])

def isVictory(ships: dict) -> bool:
    return all([s['destroyed'] for s in ships])