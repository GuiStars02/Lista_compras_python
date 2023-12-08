import os
import random

palavras = ['impressora', 'computador', 'celular', 'geladeira', 'fone', 'liquidificador']
palavra_secreta = random.choice(palavras)
letra_certa = ''
tentativas = 0
print('Bem vindo ao palavra secreta!!')
print('Todas as palvras são ELETRONICOS e ELETRODOMÉSTICOS!! Boa sorte!')

while True: 
    #Solicitar, checar e armazenar as letras que estão corretas
    letra_dig = input('Digite uma letra: ')
    tentativas += 1
    if len(letra_dig) > 1:
        print('Digite apenas UMA letra!!!')
        continue

    if letra_dig.isdigit():
        print('Digite apenas LETRAS!!!')
        continue

    if letra_dig in palavra_secreta:
        letra_certa += letra_dig
    
    #definir a variável pra vazio 
    palavra_correta = ''

    #Analisar e Organizar as letras armazenadas
    for i in palavra_secreta:
        if i in letra_certa:
            palavra_correta += i
        else:
            palavra_correta += '*'
    print(palavra_correta)

    #Reiniciar ou sair do jogo
    if palavra_correta == palavra_secreta:
        print('PARABÉNS, VOCÊ GANHOU ESTA RODADA!!')
        print(f'Tentativas: {tentativas}')
        rodada = input('Deseja continuar o jogo? [S]im ou [N]ão: ')
        if rodada.lower().startswith('s'):
            letra_certa = ''
            tentativas = 0
            palavra_secreta = random.choice(palavras)

            os.system('cls')
            continue
        
        else:
            break
