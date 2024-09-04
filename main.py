import random

def ascii_art():
    return """
  _______ _____  ______           _____ _    _ _____  ______      _    _ _    _ _   _ _______ 
 |__   __|  __ \\|  ____|   /\\    / ____| |  | |  __ \\|  ____|    | |  | | |  | | \\ | |__   __|
    | |  | |__) | |__     /  \\  | (___ | |  | | |__) | |__       | |__| | |  | |  \\| |  | |   
    | |  |  _  /|  __|   / /\\ \\  \\___ \\| |  | |  _  /|  __|      |  __  | |  | | . ` |  | |   
    | |  | | \\ \\| |____ / ____ \\ ____) | |__| | | \\ \\| |____     | |  | | |__| | |\\  |  | |   
    |_|  |_|  \\_\\______/_/    \\_\\_____/ \\____/|_|  \\_\\______|    |_|  |_|\\____/|_| \\_|  |_|   
                                                                                              
    """

print(ascii_art())
mat=[]
tentativas=10
matriz_acertou= False


for i in range(0,5):
    mat.append(0)
    mat[i]=[]
    for j in range(0,5):
        mat[i].append(0)

print("=========")
for line in mat:
    print(' '.join(str(elemento) for elemento in line))
print("=========")

posicao_linha = random.randint(0,4)
posicao_coluna = random.randint(0,4)

while tentativas > 0:
    print(f"\n-> VOCÊ TEM {tentativas} TENTATIVAS <-\n")
    linha=int(input("digite a linha (0,4): "))
    coluna=int(input("digite a coluna (0,4): "))

    if (linha == posicao_linha and coluna == posicao_coluna):
        print(mat[linha][coluna])
        print("\n|ACERTOU!|")
        mat[linha][coluna] = 'X'
        break
        
    else:
        tentativas -=1
        print("\n|ERROU!|")
        if linha < posicao_linha:
            print("-> O TESOURO ESTÁ AO NORTE! <-")
        elif linha > posicao_linha:
            print("-> O TESOURO ESTÁ AO SUL! <-")
        if coluna > posicao_coluna:
            print("-> O TESOURO ESTÁ A LESTE <-")
        elif coluna < posicao_coluna:
            print("-> O TESOURO ESTÁ A OESTE<-")

if not matriz_acertou:
    print("====================")
    print(f"o tesouro estava em {linha},{coluna}")
    mat[linha][coluna] = 'X'
    for line in mat:
        print(' '.join(str(elemento) for elemento in line))
    print("====================")

    
    


