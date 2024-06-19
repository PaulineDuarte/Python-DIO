# Um unico usuário
# criar uma variavel de deposito e depositar valores positivos
# Limite de 3 saques diarios de no maximo 500 por saque 
# exibir mensagem caso não tenha dinheiro na conta 

limite = 500 
n_saque = 0
limite_Saq=3 
saldo=0
extrato = ""

menu = """


[d] depositar
[s] sacar 
[e] Extrato 
[z] sair 

"""

while True :
    opcao = input(menu)

    if opcao == "d" :
        Deposito=float(input("Qual o valor do seu deposito: "))
        if Deposito >0 : 
            saldo+=Deposito 
            extrato +=f"O valor do seu deposito foi de : {Deposito:.2f}\n"
        else : 
            print("Operação falhou. Valor informado é invalido")

    elif opcao == "s" : 
        saque= float(input("Informe o valor do saque : "))

        if saque > limite : 
            print("Operação falhou! O valor do saque excedeu o limite")

        elif (n_saque) >= (limite_Saq) : 
            print("Operação falhou ! Número máximo de saques excedido ")

        elif saque > saldo : 
              print("Operação falhou ! Você não tem saldo suficiente")

        elif saldo > 0 : 
            saldo-=saque 
            extrato += f"saque : R$ {saque:.2f} \n"
            n_saque+= 1
        else: 
            print("Operação falhou ! O valor informado foi invalido\n") 

    elif opcao == "e" : 
            print("################# Extrato ##############")
            if not extrato : 
                print("Não houve movimentações.")
            
            else :
                print(extrato)
                print(f"Seu saldo é de R$ :  {saldo:.2f}")
                print("#################")

    elif opcao == "z": 
        break

    else : 
        print("Valor Invalido informado")

    
     
