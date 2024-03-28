menu = """

[d]depositar
[s]saldo
[e]extrato
[q]sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limete_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = int(input("Digite o valor desejado: "))
        print(f'''Foram deposotados R$ {deposito:.2f}''')
        saldo = saldo + deposito        
    elif opcao == "s":
        print(saldo)
    elif opcao == "e":
        extrato =f'''
    {saldo}
    {deposito}
    {numero_saques}
    '''
        print(extrato)
    elif opcao == "q":
        break