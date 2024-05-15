palavra_secreta = 'futuro'
tentativas = 0
formatacao = '*' * len(palavra_secreta)

while formatacao != palavra_secreta:
    letra = input('Digite uma letra: ')

    if len(letra) == 1:
        nova_formatacao = ''

        for i in range(0,len(palavra_secreta),1):
             if letra == palavra_secreta[i]:
                nova_formatacao += letra

             else: 
                nova_formatacao += formatacao[i]
        formatacao = nova_formatacao
        print(f'Palavra secreta: {formatacao}')
        
    else:
        print('Digite apenas uma letra')
    tentativas += 1
print(f'\nParabéns! \nVocê descobriu a palavra secreta! =D \n------\nNúmero de tentativas: {tentativas}')





