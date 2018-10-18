## QUESTÃO 3 ##
#
# Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César.
# 
# A cifra de César é uma simples cifra de deslocamento que se baseia na transposição 
# de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. 
# O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular. 
# A letra é deslocada para tantos valores quanto o valor da chave.
#
# A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.
#
# Um ROT13 no alfabeto latino seria o seguinte:
# 	Normal:  abcdefghijklmnopqrstuvwxyz
#	Cifrado: nopqrstuvwxyzabcdefghijklm
#
# Exemplos:
#	Entrada: ROT5 omg 
#          Saída: trl
#	Entrada: ROT0 c 
#          Saída: c
#	Entrada: ROT26 Cool 
#          Saída: Cool
#	Entrada: ROT13 The quick brown fox jumps over the lazy dog. 
#          Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#	Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
#          Saída: The quick brown fox jumps over the lazy dog.
#
# Se um valor de entrada inválido for digitado, a seguinte mensagem 
# deve ser impressa: 'Erro'. 
# Entradas inválidas podem ser entradas que contém códigos de rotações 
# inválidos ou mensagens contendo caracteres que não estão no alfabeto. 
# Exemplos:
# 	Entrada: RARA abc Saída: Erro
# 	Entrada: ROT5 c99 Saída: Erro
#
# As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', 
# ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    alfabetoMinusculo = 'abcdefghijklmnopqrstuvwxyz'
    alfabetoMaiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    entrada = input("digite a entrada: ")

    if 'ROT' in entrada:
        numero = entrada[3:5].strip()
        string = entrada[5:].strip()
        if numero.isdigit():
            chave = int(numero) 
        else:
            print('Erro')
            return
        

        tamanhoString = len(string)
        contador = 0
        stringRot = ''

        alfabetoMaiusculoRot = alfabetoMaiusculo[chave:] + alfabetoMaiusculo[:chave]
        alfabetoMinusculoRot = alfabetoMinusculo[chave:] + alfabetoMinusculo[:chave]



        while contador < tamanhoString:
            letra = string[contador]
            
            if letra.isupper():
                indiceLetra = alfabetoMaiusculo.find(letra)
                if indiceLetra == -1:
                    print("Erro")
                    return
                letraRot = alfabetoMaiusculoRot[indiceLetra]
            elif letra is " " or letra is ".":
                letraRot = letra
            else:
                indiceLetra = alfabetoMinusculo.find(letra)
                if indiceLetra == -1:
                    print("Erro")
                    return
                letraRot = alfabetoMinusculoRot[indiceLetra]

            stringRot = stringRot + letraRot
            contador += 1
        
        print(stringRot)
    else:
        print("Erro")
        



    
if __name__ == '__main__':
    main()
