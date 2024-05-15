"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ') 
numero_de_letras = (len(nome))
if numero_de_letras <= 4:
    print('Seu nome é curto')
elif numero_de_letras >= 5 and numero_de_letras <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')