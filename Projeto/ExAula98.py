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
#print(duas_parte_cpf)
nove_digitos, dois_digitos = duas_parte_cpf
#print(nove_digitos)
regressiva = 10
soma = 0
for i in nove_digitos:
    soma += int(i) * regressiva
    regressiva -= 1
#print(soma)
calculo = (soma * 10) % 11

primeiro_digito = 0 if calculo > 9 else calculo
print(primeiro_digito)

