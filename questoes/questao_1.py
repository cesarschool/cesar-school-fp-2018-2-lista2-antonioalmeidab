## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234@1, umF1#, 2w3E*, 2We3345
# Então, a saída do programa deve ser:
# ABd1234@1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
def main():
    # senhas = input("Digite as senhas: ").split(',')
    # senhasValidas = []
    # for senha in senhas:
    #     senha = senha.strip()
    #     if (len(senha) >= 6 and len(senha) <= 12):
    #         if (not senha.isupper() and not senha.islower()):
    #             if(not senha.isalpha() and not senha.isnumeric()):
    #                 if(senha.find("$") != -1 or senha.find("#") != -1 or senha.find("@") != 0):
    #                     senhasValidas.append(senha)
    # print(", ".join(senhasValidas))
    senhas = input("Digite as senhas separadas por virgulas: ")

    finalContador = len(senhas) - 1
    contador = 0
    ultimaVirgula = 0

    while contador <= finalContador:
        if senhas[contador] == ',':
            senhaAtual = senhas[ultimaVirgula:contador]
            senhaAtual = senhaAtual.strip()

            if len(senhaAtual) >=6 and len(senhaAtual) <= 12:
                if not senhaAtual.isalpha() and not senhaAtual.isnumeric():
                    if not senhaAtual.isupper() and not senhaAtual.islower():
                        if senhaAtual.find("$") != -1 or senhaAtual.find("#") != -1 or senhaAtual.find("@") != -1:
                            print(senhaAtual, end = ", ")
            ultimaVirgula = contador + 1
        elif contador == finalContador:
            senhaAtual = senhas[ultimaVirgula: finalContador + 1]
            senhaAtual = senhaAtual.strip()
            if len(senhaAtual) >=6 and len(senhaAtual) <= 12:
                if not senhaAtual.isalpha() and not senhaAtual.isnumeric():
                    if not senhaAtual.isupper() and not senhaAtual.islower():
                        if senhaAtual.find("$") != -1 or senhaAtual.find("#") != -1 or senhaAtual.find("@") != -1:
                            print(senhaAtual)
        contador += 1
                            
if __name__ == '__main__':
    main()
