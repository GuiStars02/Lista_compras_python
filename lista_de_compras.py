import os

print('**LISTA DE COMPRAS**\n')
lista = []

while True:
    #Solicitar se o user quer adicionar um produto na lista, apagar ou ver a lista
    print('Selecione uma opção')
    escolha= input('[a]dicionar  [e]xcluir  [l]istar: ')

    #Adicionar na lista de compras
    if 'a' == escolha:
        os.system('cls')
        item = input('Digite um item para inserir: ')
        lista.append(item)

    #Mostrar lista de itens
    elif 'l' == escolha:
        os.system('cls')
        for i, produto in enumerate(lista):
            print(i, produto)
    
    #Apagar item da lista
    elif 'e' == escolha:
        try:
            excluir = int(input('Digite o índice do item: '))
            lista.pop(excluir)
        except:
            print('Digite um índice válido!!\n')
    
    else:
        print('Digite "a", "e" ou "l"')
            

