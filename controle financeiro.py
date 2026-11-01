print("bem vindo ao sistema de controle financeiro, aqui você poderá cadastrar suas entradas, saídas e te darmos um resumo de suas transações financeiras")

cadastro_entrada = 0
cadastro_despesas = 0

while True:
 operacao_escolhida=input("digite 1 para cadastrar entradas \ndigite 2 para cadastrar despesas \ndigite 3 para consultar suas movimentações\ndigite 4 para consultar o seu resumo financeiro \ndigite 6 para encerrar o programa\n")

 if operacao_escolhida == "1":
  valor=float(input("digite o valor do salario: \n"))
  if valor > 0:
   cadastro_entrada += valor
   print(f"o valor  do salrio foi cadastrado com sucesso, total de entradas: {cadastro_entrada} reais")
   while True: 
      adicionar_entrada =input("adicionar mais uma entrada? (s/n):")
      if adicionar_entrada == "s":
        print("ok, vamos adicionar mais uma entrada")
        valor = float(input("digite o valor da entrada: \n"))
        if valor > 0:
         cadastro_entrada += valor
         print(f"o valor  do salrio foi cadastrado com sucesso, total de entradas: {cadastro_entrada} reais")
        else:
         print("opção invalida, por favor digite uma das opções validas") 
      elif adicionar_entrada == "n":
            print("certo,vamos encerraro cadastro de Entradas")
            break
      else:
        print("opção invalida, por favor digite uma das opções validas")
        break
  else:
   print("o valor do salario nao pode ser negativo, por favor digite um valor valido")
    
 elif operacao_escolhida == "2":
  valor = float(input("digite o valor da despesa: \n"))
  if valor > 0:
   cadastro_despesas += valor
   print(f"o valor da despesa foi cadastrado com sucesso: {cadastro_despesas} reais")
   while True: 
    adicionar_despesa =input("adicionar mais uma despesa? (s/n):")
    if adicionar_despesa == "s":
      print("ok, vamos adicionar mais uma despesa")
      valor = float(input("digite o valor da despesa: \n"))
      if valor > 0:
       cadastro_despesas += valor
       print(f"o valor da despesa foi cadastrado com sucesso: {cadastro_despesas} reais")
      else:
       print("opção invalida, por favor digite uma das opções validas")

    elif adicionar_despesa == "n":
      print("certo,vamos encerraro cadastro de despesas")
      break
    else:
            print("opção invalida, por favor digite uma das opções validas")
            break
  else:
   print("o valor da despesa não pode ser nagativo, por favor digite um valor valido")
    
 elif operacao_escolhida == "3":
   print("consultando suas movimentações...")
   print(f"suas entradas foram: {cadastro_entrada}")
   print(f"suas despesas foram: {cadastro_despesas}")
 elif operacao_escolhida == "4":
   print("consultando seu resumo financeiro...")
   saldo = cadastro_entrada - cadastro_despesas
   print(f"seu saldo atual é de: {saldo} Reais\n")

 elif operacao_escolhida == "6":
   print("encerrando o programa, obrigado por utilizar nosso sistema de controle financeiro")
   break
 
 else:
   print("operação invalida, por favor digite uma das opções validas")
   
