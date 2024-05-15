def generator(n=0):
    yield 1 #pausar
    print('Continuando...')
    yield 2

gen = generator(n=0)
# print(next(gen))
# print(next(gen))

for n in gen:
    print(n)