frase = '   Olha só que   , coisa interessante   '
lista_frases_cruas = frase.split(',')

listas_frases = []
for i, frase in enumerate(lista_frases_cruas):
    listas_frases.append(lista_frases_cruas[i].strip())

#print(lista_frases_cruas)
#print(listas_frases)

frases_unidas = '-'.join(listas_frases)
print(frases_unidas)