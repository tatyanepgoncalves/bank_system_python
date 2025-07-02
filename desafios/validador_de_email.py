# Entrada do usuário
email = input().strip()
# TODO: Verifique as regras do e-mail:
while True: 

  if " " in email:
    print("E-mail inválido")
    break
  

  # Deve conter o caractere "@"
  elif "@" not in email:
    print("E-mail inválido")
    break

  # Não pode começar ou terminar com "@"
  elif email.startswith("@") or email.endswith("@"):
    print("E-mail inválido")
    break

  # Deve conter um domínio (ex: gmail.com)
  elif len(email.split("@")) != 2:  # Garante que há apenas um "@" e que há algo antes e depois
      print("E-mail inválido")
      break 


  elif "." not in  email.split("@")[1]: # Verifica se o domínio possui um ponto
      print("E-mail inválido")
      break 
  
  elif email.split("@")[1].startswith(".") or email.split("@")[1].endswith("."): # Verifica se o domínio não começa ou termina com ponto
        print("E-mail inválido")
        break

  # Se todas as verificações passaram
  else: 
    print("E-mail válido")
    break
