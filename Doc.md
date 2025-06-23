# Documentação das Funções do Projeto Batalha Naval

## main.py
- **main**: Ponto de entrada do jogo. Inicializa variáveis, cria navios, tabuleiros, gerencia o loop principal e reinício do jogo.

## src/board.py
- **createBoard(size=10, ships=None)**: Cria o tabuleiro visível e o tabuleiro com os navios posicionados, garantindo que não haja sobreposição ou navios fora do tabuleiro.
- **updateBoard(visible_board, ships)**: Atualiza o tabuleiro visível, marcando as posições dos navios destruídos com '+'.

## src/game.py
- **colLetterToIndex(letter)**: Converte uma letra de coluna (ex: 'A') para o índice numérico correspondente.
- **clearScreen()**: Limpa a tela do terminal.
- **color(char)**: Retorna o caractere colorido para exibição no terminal.
- **printBoard(board)**: Exibe o tabuleiro visível para o jogador, com cores.
- **printRealBoard(real_board)**: Exibe o tabuleiro real (com navios) para depuração.
- **printGameOver()**: Exibe mensagem de derrota.
- **printVictory()**: Exibe mensagem de vitória.
- **askRetry()**: Pergunta ao usuário se deseja jogar novamente.
- **difficulty()**: Pergunta ao usuário o nível de dificuldade e retorna a escolha.
- **inputCoord(board_size)**: Solicita e valida a entrada de coordenadas do usuário.
- **mainLoop(visible_board, board_size, ships, ships_board, attemps)**: Gerencia o loop de jogadas, atualiza o estado do jogo e retorna se o jogador venceu.

## src/move_and_rules.py
- **defineDifficulty(difficulty)**: Retorna o número de tentativas baseado na dificuldade escolhida.
- **verifyAttemps(attemps)**: Verifica se ainda há tentativas restantes.
- **bomb(x, y, visible_board, ships_board)**: Realiza o ataque na posição escolhida, marcando acerto ('X') ou erro ('O').
- **destroyedShips(ships)**: Conta quantos navios já foram destruídos.
- **isVictory(ships)**: Verifica se todos os navios foram destruídos.

## src/ship.py
- **resetStats()**: Reseta as posições ocupadas por navios.
- **createShip(name, size, pos=None, direction=None, letter=None, board_size=10)**: Cria um dicionário representando um navio, sorteando posição e direção válidas se necessário.
- **getShipPos(pos, direction, size)**: Retorna todas as posições ocupadas por um navio.
- **updateShip(ship, board)**: Marca o navio como destruído se todas as suas posições foram atingidas.
- **updateShips(ships, board)**: Atualiza o estado de todos os navios.
- **randomPos(size, direction, board_size)**: Gera uma posição inicial aleatória válida para um navio.
- **randomDir()**: Sorteia aleatoriamente a direção (horizontal ou vertical) de um navio.
