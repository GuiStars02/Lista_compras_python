# Calculadora simples
import os

print('Calculadora')

while True: 
    #Solicitar os dados necessários para a conta
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operacao = input('Digite o sinal de operação "+", "-", "*" ou "/": ')

# tentar converter os dados para números de ponto flutuante
    try:
        numero1_float = float(numero_1)
        numero2_float = float(numero_2)

    except:
        print('Digite apenas números válidos!!!')
        continue
#Verificar quantidade de operadores
    if len(operacao) > 1:
        print('Por favor, digite apenas um operador')
        continue

    print('Realizando sua conta...')
#Contas
    if operacao == '+':
        print(f'{numero1_float} + {numero2_float} = {numero1_float + numero2_float}')
    
    elif operacao == '-':
        print(f'{numero1_float} - {numero2_float} = {numero1_float - numero2_float}')

    elif operacao == '*':
        print(f'{numero1_float} * {numero2_float} = {numero1_float * numero2_float}')

    elif operacao == '/':
        print(f'{numero1_float} / {numero2_float} = {numero1_float / numero2_float}')

    else: 
        print('Digite um sinal de operação válido!!')
        continue    
    
    #Opção de saída
    saida= input('Deseja sair da calculadora? Pressione [S]im para sair ou [N]ão para continuar: ').lower()
    if saida.startswith('s'):
        break

    os.system('cls')