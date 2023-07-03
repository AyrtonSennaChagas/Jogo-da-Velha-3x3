# Jogo da velha em python

# Função para imprimir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
  print("-------------")
  for i in range(3):
    print("|", end="")
    for j in range(3):
      print(" " + tabuleiro[i][j] + " |", end="")
    print("\n-------------")

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro):
  # Verificar linhas
  for i in range(3):
    if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != " ":
      return tabuleiro[i][0]
  # Verificar colunas
  for j in range(3):
    if tabuleiro[0][j] == tabuleiro[1][j] == tabuleiro[2][j] != " ":
      return tabuleiro[0][j]
  # Verificar diagonais
  if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
    return tabuleiro[0][0]
  if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != " ":
    return tabuleiro[0][2]
  # Verificar se há espaços vazios
  for i in range(3):
    for j in range(3):
      if tabuleiro[i][j] == " ":
        return None
  # Se não houver vencedor nem espaços, é um empate
  return "Empate"

# Função para validar a jogada do usuário
def validar_jogada(jogada, tabuleiro):
  # Verificar se a jogada é um número entre 1 e 9
  if not jogada.isdigit() or int(jogada) < 1 or int(jogada) > 9:
    print("Jogada inválida. Digite um número entre 1 e 9.")
    return False
  # Verificar se a posição está livre
  i = (int(jogada) - 1) // 3
  j = (int(jogada) - 1) % 3
  if tabuleiro[i][j] != " ":
    print("Jogada inválida. Essa posição já está ocupada.")
    return False
  # Se passar nas verificações, a jogada é válida
  return True

# Função principal do jogo
def jogo_da_velha():
  # Inicializar o tabuleiro com espaços vazios
  tabuleiro = [[" ", " ", " "] for i in range(3)]
  
  # Definir os símbolos dos jogadores
  jogador1 = "X"
  jogador2 = "O"

  # Definir o jogador atual e o vencedor
  jogador_atual = jogador1
  vencedor = None

  # Imprimir as instruções do jogo
  print("Bem-vindo ao jogo da velha em python!")
  print("O tabuleiro tem as seguintes posições:")
  print("-------------")
  print("| 1 | 2 | 3 |")
  print("-------------")
  print("| 4 | 5 | 6 |")
  print("-------------")
  print("| 7 | 8 | 9 |")
  print("-------------")
