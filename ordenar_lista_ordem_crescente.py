lista = [3, 9, 2, 4, 3, 7, 8, 1]
fim = len(lista)
while True:
    x = 0
    trocou = False
    while x < (fim-1):
        if lista[x] > lista[x+1]:
            trocou = True
            temp = lista[x+1]
            lista[x+1] = lista[x]
            lista[x] = temp
        x += 1
    if not trocou:
        break
for c in lista:
    print(c, end=' ')