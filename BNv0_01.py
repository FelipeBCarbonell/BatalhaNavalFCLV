import random

LpN = {
    'A' : 1,
    'B' : 2,
    'C' : 3,
    'D' : 4,
    'E' : 5,
    'F' : 6,
    'G' : 7,
    'H' : 8,
    'I' : 9,
    'J' : 10,
}

Barcos = [['oi', 2], ['tchau', 5]]

MatrizPadrao = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

def DefineBarcosBot():
    Matriz = MatrizPadrao
    for barco in Barcos:
        Passou = True
        while Passou:
            linha = random.choice([0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9])
            coluna = random.choice([0, 1, 2, 3, 4, 5, 6 ,7 ,8 ,9])
            orientacao = random.choice(['h', 'v'])
            if orientacao == 'h':
                OverLap = False
                if barco[1] + coluna > 10:
                    Deny = True
                else:
                    for i in range(barco[1]):
                        if Matriz[linha][coluna+i] != 0:
                            Deny = True
                            OverLap = True
                    if OverLap == False:
                        Passou = False
                        for i in range(barco[1]):
                            Matriz[linha][coluna+i] = 1
            elif orientacao == 'v':
                OverLap = False
                if barco[1] + linha > 10:
                    Deny = True
                else:
                    for i in range(barco[1]):
                        if Matriz[linha+i][coluna] != 0:
                            Deny = True
                            OverLap = True
                    if OverLap == False:
                        Passou = False
                        for i in range(barco[1]):
                            Matriz[linha+i][coluna] = 1
    return Matriz

def Tiro(Matriz, Linha, Coluna):
    if Matriz[Linha-1][LpN[Coluna]-1] == -1 or Matriz[Linha-1][LpN[Coluna]-1] == -2:
        return 'Isso já foi selecionado'
    elif Matriz[Linha-1][LpN[Coluna]-1] == 0:
        return 'água'
    elif Matriz[Linha-1][LpN[Coluna]-1] == 1:
        return 'navio'
 
def DefineBarcos():
    Matriz = MatrizPadrao
    for barco in Barcos:
        print('{0} possui {1} de tamanho'.format(barco[0], barco[1]))
        Passou = True
        while Passou:
            linha = int(input('Qual linha? (1 - 10)')) - 1
            coluna = LpN[input('Qual coluna? (A - J)')] - 1
            orientacao = input('Qual orientação? (h ou v)')
            if orientacao == 'h':
                OverLap = False
                if barco[1] + coluna > 10:
                    print('indisponível')
                else:
                    for i in range(barco[1]):
                        if Matriz[linha][coluna+i] != 0:
                            print('indisponível')
                            OverLap = True
                    if OverLap == False:
                        Passou = False
                        for i in range(barco[1]):
                            Matriz[linha][coluna+i] = 1
            elif orientacao == 'v':
                OverLap = False
                if barco[1] + linha > 10:
                    print('indisponível')
                else:
                    for i in range(barco[1]):
                        if Matriz[linha+i][coluna] != 0:
                            print('indisponível')
                            OverLap = True
                    if OverLap == False:
                        Passou = False
                        for i in range(barco[1]):
                            Matriz[linha+i][coluna] = 1
    return Matriz
 
MatrizPlayer = DefineBarcos()
MatrizPadrao = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
MatrizBot = DefineBarcosBot()
MatrizObservada = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]

game = True
 
while game:
    # Mostrar Tabuleiro
    # Pedir Tiro
    # Ver se Player ganhou - game = False
    # Mostrar Tabuleiro
    # Tiro do Bot
    # Ver se Bot ganhou - game = False
    x = 0
