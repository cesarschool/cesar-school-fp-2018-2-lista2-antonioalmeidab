## QUESTÃO 2 ##
#
# Um robô se move em um plano a partir do ponto original (0,0). O robô pode se 
# mover nas direções CIMA, BAIXO, ESQUERDA e DIREITA de acordo com um 
# passo fornecido. O traço do movimento do robô é mostrado da seguinte forma:
#
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Os números após a direção são passos. 
# Escreva um programa para calcular a distância entre a posição atual e o 
# ponto original após uma seqüência de movimentos. Se a distância for um 
# float, basta imprimir o inteiro mais próximo.
# Exemplo:
# Se as seguintes tuplas são dadas como entrada para o programa:
# 
# CIMA 5
# BAIXO 3
# ESQUERDA 3
# DIREITA 2
#
# Então, a saída do programa deve ser:
# 2
# 
# Dicas:
# As entradas devem ser lidas do console até que um valor vazio seja digitado. 
# A saída deve ser um inteiro que representa a distancia para o ponto original. 
# Entradas inválidas devem ser descartadas da contagem.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    up = 'CIMA'
    down = 'BAIXO'
    right = 'DIREITA'
    left = 'ESQUERDA'
    x = y = 0
    comando = 1

    while(comando != '0'):
        comando = input("Digite a direção e o passo (0 para sair): ").upper()
        
        if comando[:len(up)] == 'CIMA':
            y = y + int(comando[5:])
        if comando[:len(down)] == 'BAIXO':
            y = y - int(comando[6:])
        if comando[:len(right)] == 'DIREITA':
            x = x + int(comando[8:])
        if comando[:len(left)] == 'ESQUERDA':
            x = x - int(comando[9:])

        # if comando.find("CIMA") != -1:
        #     y = y + int(comando[5:])
        # if comando.find("BAIXO") != -1:
        #     y = y - int(comando[6:])
        # if comando.find("DIREITA") != -1:
        #     x = x + int(comando[8:])
        # if comando.find("ESQUERDA") != -1:
        #     x = x - int(comando[9:])
    
    distancia = (x**2 + y**2)**(1/2)
    print("A distância percorrida foi: ", int(distancia))



    # if comando[:len('CIMA')] == 'CIMA':
    #     cont += 1

if __name__ == '__main__':
    main()
