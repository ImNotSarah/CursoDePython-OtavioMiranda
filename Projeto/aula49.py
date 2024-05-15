numero_str = input('Vou dobrar o numero que vc digitar: ')

#print(numero_str.isdigit()) #verifica se os caracteres são numeros

try:
    numero_float = float(numero_str) #executa o código até o primeiro erro aparecer
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('isso não é um número') #quando o erro aparece ele pula para o except

#if numero_str.isdigit():
#    numero_float = float(numero_str)
#    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
#else:
#    print('isso não é um número')
