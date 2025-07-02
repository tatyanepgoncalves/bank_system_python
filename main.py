menu = """
Bem vindo ao sistema bancário Lobs.

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Com base nas opções acima insira uma letra: 
"""

account_balance = 0 # Saldo
account_limit = 500 # Limite
account_statement = "" # Extrato
withdrawal_number = 0 # Número de 
WITHDRAWAL_LIMIT = 3 # Limite de saques

value_count = 0 # Valor da conta
value_deposit = [] # Valor do depósito
statement = value_deposit 


while True: 
  option = input(menu)

  if option == "d":
    value = float(input("Digite o valor para o depósito: "))

    if value > 0:
      account_balance += value
      account_statement += f"Depóstito de R$ {value:.2f}\n"

    else:
      print("Operação falhou! O valor informado é inválido.")
  
  
  elif option == "s":
    value = float(input("Digite o valor para saque: "))

    exceeded_balance = value > account_balance
    exceeded_limit = value > account_limit
    exceeded_withdrawal = withdrawal_number >= WITHDRAWAL_LIMIT

    if exceeded_balance:
      print("Operação falhou! Você não tem saldo suficiente.")

    elif exceeded_limit:
      print("Operação falhou! O valor do saque excede o limite.")
    
    elif exceeded_limit:
      print("Operação falhou! Você já atingiu o limite de saques.")
    
    elif value > 0:
      account_balance -= value
      account_statement += f"Saque de R$ {value:.2f}\n"
      withdrawal_number += 1
    
    else:
      print("Operação falhou! O valor informado é invalido.")
  
  elif option == "e":
    print("\n================ EXTRATO =================")
    print("Não foram realizadas movimentações." if not account_statement else account_statement)
    print(f"\nSaldo: R$ {account_balance:.2f}")
    print("================================")
  
  elif option == "q":
    print("Saindo do sistema... Até a próxima!")
    break

  else: 
    print("Opção inválida, por favor selecione novamente a operação desejada.")