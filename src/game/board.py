def createBoard(size: int = 10, ships: list[dict] = None) -> list[list[str]]:
    board = [["~" for _ in range(size)] for _ in range(size)]
    ships_board = [["~" for _ in range(size)] for _ in range(size)]
    ocupados = set()  # Conjunto de posições já ocupadas

    if ships:
        for ship in ships:
            x, y = ship['pos']
            positions = []

            for i in range(ship['size']):
                pos = (x + i, y) if ship['direction'] == 0 else (x, y + i)

                if pos[0] >= size or pos[1] >= size:
                    raise ValueError(f"Navio '{ship['name']}' ultrapassa o tabuleiro na posição {pos}.")
                if pos in ocupados:
                    raise ValueError(f"Navio '{ship['name']}' está sobrepondo outro navio na posição {pos}.")

                positions.append(pos)

            # Marca no tabuleiro e adiciona ao conjunto
            for px, py in positions:
                ships_board[py][px] = ship['letter']
                ocupados.add((px, py))

    return board, ships_board
