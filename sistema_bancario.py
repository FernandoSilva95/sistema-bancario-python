print("Bem vindo ao seu banco!")
saldo_inicial = float(input("Qual o seu saldo inicial? R$ "))
print(f"O seu saldo inicial é R$ {saldo_inicial}")
saldo_atual = 0
saldo_atual += saldo_inicial
numero_saques = 0
limite_saque_diario = 500
LIMITE_SAQUES = 3
extrato = ""
      
print("""
      ***********MENU***********

      [1] - Depositar
      [2] - Sacar
      [3] - Extrato
      [4] - Cancelar

      **************************
""")

while True:
    
    opcao = int(input("Informe uma opção: "))
    
    if opcao == 1:
        valor = float(input("Informe o valor do depósito: R$ "))

        if valor > 0:
           saldo_atual += valor
           extrato += f"Depósito: R$ {valor:.2f}\n"
           print("Depósito realizado com sucesso!")
           
        else:
            print("Seu depósito falhou. Tente novamente!")

    elif opcao == 2:
        
        valor = float(input("Informe o valor do saque: R$ "))
        
        excedeu_saldo = valor > saldo_atual
        
        excedeu_limite = valor > limite_saque_diario
        
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação inválida. Você não possui saldo suficiente.")
            
        elif excedeu_limite:
            print("Operação inválida. Você excedeu o limite diário.")
            
        elif excedeu_saques:
            print("Operação inválida. Número máximo de saques excedido.")
        
        elif valor > 0:            
            saldo_atual -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")  
            
        else:
            print("Saldo insuficiente!")
    
    elif opcao == 3:
        print("\n*************EXTRATO**************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo_atual:.2f}")
        print("\n**********************************")
        
    elif opcao == 4:
        print("Operação cancelada.")
    
    else:
        break
  