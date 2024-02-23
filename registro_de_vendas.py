from exercicio115.lib.interface import *

estoque = {
    'alfase':[100, 2.50],
    'tomate':[120, 1.50],
    'cebola':[150, 2],
    'bolacha':[200, 3,10]
}
vendas = []
cont = 0
cabeçalho('Caixa de supermercado')
#entrada de valores de compra
while True:
    while True:
        p = str(input('qual o produto[nenhum para!]:'))
        if p in estoque.keys() or p.upper() == 'NENHUM':
            break
        else:
            print('O produto escolhido não foi encontardo, tente novamente!')
            linha()
    if p.upper() == 'NENHUM':
        break
    v = int(input('quantos produtos:'))
    linha()
    vendas.append([])
    vendas[cont].append(p)
    vendas[cont].append(v)
    cont += 1
total = 0

#Operação de vendas
cabeçalho('Compras')
for operacao in vendas:
#declaração de variaveis
    produto, quantidade = operacao
    valor = estoque[produto][1]
    preço = valor * quantidade
#Mostrar informações de compra
    print(f'{produto} : {quantidade} x {valor} = {preço}')
    estoque[produto][0] -= quantidade
#Incremento
    total += preço
linha()
#Valor da compra
print(f'valor total da compra: {total}')

#printa o estoque dos produtos
cabeçalho('Estoque')
for k, v in estoque.items():
    print(f'produto: {k}\n Quantidade: {v[0]}\n Preço:{v[1]}')
    linha()




