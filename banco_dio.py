
caixa = '''
    OPÇÕES:
    DEPÓSITO : [d]
    SAQUE: [s]
    EXTRATO: [e]
    SAIR: [q]
    '''

saldo = 1500
extrato = 0
saque_diario = 3

while True:

  print(caixa)
  opcao = input('escolha uma destas opções: ')
  #depósito
  if opcao == 'd':
    #não pode ser negativo
    valor_deposito = float(input('Valor de depósito: '))
    if valor_deposito > 0:
      saldo += valor_deposito
      print(f'Valor depositador de: R${valor_deposito:.2f}')
      print(f'Seu saldo é de: R${saldo:.2f}')

    else:
      print('Não é permitido este valor')

  #saque
  elif opcao == 's':
    #verificando limite de saque
    if saque_diario > 0:
      valor_sacado = float(input('Valor de saque: '))
      #não pode ser nagativo
      if valor_sacado > 0:
        if saldo - valor_sacado < 0:
          print('Você não tem saldo suficiente')
        else:
          saldo -= valor_sacado
          saque_diario = saque_diario - 1
          print(f'Vocẽ sacou: R${valor_sacado:.2f}')
          print(f'Seu saldo é de: R${saldo:.2f}')


      else:
        print('Este valor não pode ser sacado')
    else:
      print('Expirou a quantidade de saques diários')


  #extrato
  elif opcao == 'e':
    linha = '-'*50
    total_saldo =f'R${saldo:.2f}'
    extrato = f'''
    QUANTIDADE DE SAQUES: {saque_diario} \n
    SALDO:\n
    {linha}
    {total_saldo.center(50,'x')}
    {linha}
    '''
    print(extrato)
 #saída
  elif opcao == 'q':
    print('Saindo do sistema')
    break
  else:
    print('Opção inválida')
 
