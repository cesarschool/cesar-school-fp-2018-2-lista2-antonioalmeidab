## QUESTÃO 4 ##
#
# Escreva um programa que leia uma data do usuário e calcule seu sucessor imediato.
# Por exemplo, se o usuário inserir valores que representem 2013-11-18, seu programa 
# deve exibir uma mensagem indicando que o dia imediatamente após 2013-11-18 é 
# 2013-11-19. Se o usuário inserir valores que representem 2013-11-30, o programa deve 
# indicar que o dia seguinte é 2013-12-01. Se o usuário inserir valores que representem 
# 2013-12-31 então o programa deve indicar que o dia seguinte é 2014-01-01. A data 
# será inserida em formato numérico com três instruções de entrada separadas; 
# uma para o ano, uma para o mês e uma para o dia. Certifique-se de que o seu programa 
# funciona corretamente para anos bissextos.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    ERRO = 'Data inválida!'
    data = input("Digite uma data(forma aaaa-mm-dd): ")
    ano = int(data[:4])
    mes = int(data[5:7])
    dia = int(data[8:])

    if mes > 12:
        print(ERRO)
    else:
        if mes == 2:
            if dia > 29:
                print(ERRO)
            elif ano%4 == 0 and ano%100 != 0 or ano%400 == 0:
                if dia <= 28:
                    print("{}-{:02d}-{:02d}".format(ano, mes, dia+1))
                else:
                    print("{}-{:02d}-01".format(ano, mes+1))
            else:
                if dia > 28:
                    print(ERRO)
                elif dia <= 27:
                    print("{}-{:02d}-{:02d}".format(ano, mes, dia +1))
                else:
                    print("{}-{:02d}-01".format(ano, mes+1))

        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            if dia > 31:
                print (ERRO)
            elif dia <= 30:
                print("{}-{:02d}-{:02d}".format(ano, mes, dia + 1))
            else:
                if mes == 12:
                    print("{}-01-01".format(ano + 1))
                else:
                    print("{}-{:02d}-01".format(ano, mes+1))
        
        else:
            if dia > 30:
                print(ERRO)
            elif dia <= 29:
                print("{}-{:02d}-{:02d}".format(ano, mes, dia +1 ))
            else:
                print("{}-{:02d}-01".format(ano, mes + 1))
            

            


    
if __name__ == '__main__':
    main()
