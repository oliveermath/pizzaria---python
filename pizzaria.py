# Mensagem principal, com as boas-vindas e cardápio com preços, tamanhos e sabores.
print(10 * '-', 'Bem vindo a Pizzaria PizzaSaborosa', 10 * '-')
print(57 * '>')
print(25 * '-', 'Cardápio', 20 * '-')

print('---''  ''Preços por tamanho (P - Pequeno)') 
print('---''  ''Preços por tamanho (M - Média)')  
print('---''  ''Preços por tamanho (G - Grande)')  

print(40 * '.')

print('---' ' ' '-' 'Pizza Salgada (P)' '  ''|''  ' 'R$ 30.00')  
print('---' ' ' '-' 'Pizza Salgada (M)' '  ''|''  ' 'R$ 45.00')
print('---' ' ' '-' 'Pizza Salgada (G)' '  ''|''  ' 'R$ 60.00')

print(40 * '.')

print('---' ' ' '-' 'Pizza Doce (P)' '  ''|''  ' 'R$ 34.00')  
print('---' ' ' '-' 'Pizza Doce (M)' '  ''|''  ' 'R$ 48.00')
print('---' ' ' '-' 'Pizza Doce (G)' '  ''|''  ' 'R$ 66.00')

# Atribuindo uma variavel para o preço e uma variavel para o valor total, 
# assim contribuindo para somatória do total.
preco_item = 0 
valor_total = 0

print(40 * '-')

while True: # Entrando no laço do sistema
    sabor = input('> Entre com o sabor desejado (PD/PS): ').upper() # Entrada do sabor, 
    # com uma função de formatação (upper).

    if sabor not in ('PS', 'PD'): 
        print(f'> Sabor inválido. Tente novamente!') 
        continue # Se o sabor digitado não estiver "entre" (PS - Pizza Salgada) e (PD - Pizza Doce)
        # ele volta o loop

    print(40 * '-')
    tamanho = input('> Digite o tamanho desejado (P - Pequeno / M - Médio / G - Grande): ').upper() # Entrada do tamanho, 
    # com uma função de formatação (upper).


    if tamanho not in ('P', 'M', 'G',):
        print('> Tamanho inválido. Tente novamente!')
        continue # Se o tamanho digitado não estiver "entre" (P - Pequeno), (M - Média) ou (G - Grande)
        # ele volta o loop

    if sabor == 'PS': # Se o sabor for (PS)
        
        # Estamos atribuindo o preço, para a variavel (preco_item) a cada tamanho diferente.
        if tamanho == 'P': 
            preco_item = 30.00
        elif tamanho == 'M':
            preco_item = 45.00
        elif tamanho == 'G':
            preco_item = 60.00

    elif sabor == 'PD': # Se o sabor for (PD)
        
        # Estamos atribuindo o preço, para a variavel (preco_item) a cada tamanho diferente.
        if tamanho == 'P':
            preco_item = 34.00
        elif tamanho == 'M':
            preco_item = 48.00
        elif tamanho == 'G':
            preco_item = 66.00
    
    valor_total += preco_item # Estamos acumulando para o (valor_total)

    # Mensagem de confirmação de pedido
    if sabor == 'PS': 
        print(f'> Você pediu uma Pizza Salgada no tamanho {tamanho} no valor de R${preco_item:.2f} reais.')
    else:
        print(f'> Você pediu uma Pizza Doce no tamanho {tamanho} no valor de R${preco_item:.2f} reais.')

    print(20 * '-')
    print(20 * '.')

     # Ao finalizar, perguntamos se o usuario quer realizar outro pedido
     # para que entre no loop novamente
    continuar = input('> Deseja mais alguma coisa? (S/N): ').upper()
    

    if continuar != ('S'): # Se a entrada for diferente de ('S' - Sim) ou seja, ('não')
        break # Laço encerrado, caso for (sim) o loop é ativado novamente.

print(30 * '-')
print(30 * '>')

# Mensagem final com o valor total do pedido.
print(f'> O valor total a pagar é: R${valor_total:.2f} reais') 
