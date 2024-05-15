
cpf = '746.824.890-70'
cpf_com_traço =''
for i in cpf:
    if i == '.':
        i = ''
        cpf_com_traço += i
    else:
        cpf_com_traço += i
#print(cpf_com_traço)       
duas_parte_cpf = cpf_com_traço.split('-')
digitos_cpf = ''.join(duas_parte_cpf)
#print(digitos_cpf)
nove_digitos = digitos_cpf[:9]
#print(nove_digitos)
contador_regressivo1 = 0
soma1 = 0
for i in nove_digitos:
    i =int(i)
    i = i * (10 - contador_regressivo1)
    contador_regressivo1 += 1
    soma1 += i
#print(soma)
calculo = (soma1 * 10) % 11

primeiro_digito = 0 if calculo > 9 else calculo
#print(primeiro_digito)

nove_e_primeiro_digitos = str(nove_digitos) + str(primeiro_digito)
#print(nove_e_primeiro_digitos)

contador_regressivo2 = 11
soma2 = 0
for i in nove_e_primeiro_digitos:
    i =int(i)
    i = i * contador_regressivo2
    contador_regressivo2 -= 1
    soma2 += i
#print(soma2)
calculo2 = (soma2 * 10) % 11
segundo_digito = 0 if calculo2 > 9 else calculo2
#print(segundo_digito)

novo_cpf = f'{nove_digitos}{primeiro_digito}{segundo_digito}'

if novo_cpf == digitos_cpf:
    print(f'{digitos_cpf} é válido')
else:
    print('CPF inválido')