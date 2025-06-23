# Batalha Naval Python

## Atividade da disciplina de **Algoritmos**

Aluno: Kauã Felipe Martins  
Professor: Anderson Paulo Avila Santos  
Curso: Ciência de Dados e IA  
Data: 23/06/2025  

---

## Sobre o Jogo

Este projeto implementa o clássico jogo Batalha Naval em Python, jogado no terminal. O objetivo é encontrar e destruir todos os navios escondidos no tabuleiro, escolhendo coordenadas para atacar. O jogo informa se o tiro foi na água, acertou ou destruiu um navio. O jogador vence ao destruir todos os navios antes de acabar as tentativas.

### Regras Básicas
- O tabuleiro é uma grade 10x10.
- Existem diferentes tipos de navios, cada um com tamanho e símbolo próprio.
- O jogador escolhe a dificuldade (número de tentativas).
- A cada rodada, o jogador informa as coordenadas para atacar.
- O jogo mostra o progresso, navios destruídos e tentativas restantes.
- O jogo termina com vitória (todos navios destruídos) ou derrota (tentativas esgotadas).

## Como Rodar o Jogo

1. Certifique-se de ter o Python 3 instalado.
2. No terminal, navegue até a pasta `src` do projeto.
3. Execute o comando:

    ```bash
    python main.py
    ```

4. Siga as instruções exibidas no terminal para jogar.

---

## Estrutura dos Arquivos
- [`main.py`](./main.py): Ponto de entrada do jogo.
- [`src/game.py`](./src/game.py): Funções de controle do jogo e interface.
- [`src/move_and_rules.py`](./src/move_and_rules.py): Regras, tentativas e ataques.
- [`src/board.py`](./src/board.py): Funções para criar e exibir tabuleiros.
- [`src/ship.py`](./src/ship.py): Criação e atualização dos navios.

Para detalhes de cada função, consulte o arquivo [`Doc.md`](./Doc.md).

