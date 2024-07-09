

def menu ():

    menu= """

    [d] depositar
    [s] sacar 
    [e] Extrato 
    [nu] Novo Usuario
    [cc] Criar Conta
    [z] sair 

    """
    return input(menu)

def deposito_conta (saldo,valor,extrato,/):
            if valor >0 : 
                saldo+=valor 
                extrato +=f"O valor do seu deposito foi de : {valor:.2f}\n"
            else : 
                print("Operação falhou. Valor informado é invalido")
            return saldo , extrato 


def saque_conta (*,saldo,valor,extrato,limite,n_saques,limite_saq) :

        if valor > limite : 
            print("Operação falhou! O valor do saque excedeu o limite")

        elif (n_saque) >= (limite_saq) : 
            print("Operação falhou ! Número máximo de saques excedido ")

        elif valor > saldo : 
              print("Operação falhou ! Você não tem saldo suficiente")

        elif saldo > 0 : 
            saldo-=valor 
            extrato += f"saque : R$ {valor:.2f} \n"
            n_saque+= 1
        else: 
            print("Operação falhou ! O valor informado foi invalido\n") 
        return saldo, extrato

def mostra_extrato (saldo,/,*,extrato):
        if not extrato : 
                    print("Não houve movimentações.")
                
        else :
             print(extrato)
             print(f"Seu saldo é de R$ :  {saldo:.2f}")
             print("#################")
        return saldo , extrato

def criar_usuario (usuarios):
        cpf=input("Informe o CPF (somente numeros): ")
        usuario=filtra_usuario(cpf,usuarios)

        if usuario:
            print("\n Já existe usuário com esse CPF")
            return 

        nome=input("Informe o nome completo: ")
        data_nasc=input("Informe sua data de nascimento (dd-mm-aaaa): ")
        endereco=input(" Informe o endereço (Logadouro,nm - bairro - cidade/sigla estado): ")

        usuarios.append({"nome": nome, "data_nascimento":data_nasc,"cpf":cpf,"endereco":endereco})
        print(" Usuario criado com sucesso !!")

def filtra_usuario(cpf,usuarios): 
     usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf] 
     return usuarios_filtrados[0] if usuarios_filtrados  else None 

def criar_conta (agencia,numero_conta,usuarios):
    cpf=input("Informe o CPF (somente numeros): ")
    usuario=filtra_usuario(cpf,usuarios)

    if usuarios : 
        print("\n**Conta Criada com Sucesso**")
        return {"agencia":agencia, "numero_conta":numero_conta , "usuario":usuarios}
    print("\n --- Usuário não encontrado ---" )

def main() : 
    limite = 500 
    agencia="0001"


    n_saque = 0
    limite_saq=3 
    saldo=0
    extrato = ""
    usuarios=[]
    contas=[]
    

    while True : 
          opcao = menu()

          if opcao == "d" : 
                valor = float(input("Qual o valor do deposito: "))

                saldo,extrato = deposito_conta(saldo,valor,extrato) 

          elif opcao == "s" : 
           valor = float(input("Qual o valor do saque: "))

           saldo,extrato = saque_conta (saldo = "saldo",valor="valor" ,limite="limite",limite_saq="limite_saq",n_saques="n_saque",
                extrato="extrato")
           
          elif opcao == "e": 
               saldo , extrato = mostra_extrato (saldo, extrato=extrato)
            

          elif opcao =="nu" : 
                criar_usuario(usuarios)
          elif opcao == "cc": 
                numero_conta= len(contas) +1 
                conta = criar_conta(agencia,numero_conta,usuarios)

                if conta : 
                      contas.append(conta)

          elif opcao == "z": 
               break
        
          else : 
                 print("Valor Invalido informado") 


main ()