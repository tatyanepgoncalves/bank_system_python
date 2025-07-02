# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input("Digite o preço original: ").strip())
cupom = input("Digite o cumpom de desconto: ").strip()

# TODO: Aplique o desconto se o cupom for válido:
if (cupom == "DESCONTO10"): 
  newValue = preco - (preco * 0.1)
  print(f"O valor do produto é R$ {newValue:.2f}")

elif (cupom == "DESCONTO20") :
  newValue = preco - (preco * 0.2)
  print(f"O valor do produto é R$ {newValue:.2f}")


elif (cupom == "SEM_DESCONTO"):
  
  print(f"O valor do produto é ${preco:.2f}")


else:
  print(f"Sem cumpom o produto é ${preco:.2f}")
