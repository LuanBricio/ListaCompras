produtos = []
quantidades = []

while True:
    produto_nomes = input('Digite o nome do produto que deseja por na lista (digite "1" para sair):')
    if produto_nomes == '1':
        break
    else:
        produtos.append(produto_nomes)
        quant_num = int(input('digite a quantide que deseja comprar:'))
        quantidades.append(quant_num)


print(produtos)
print(quantidades)

arquivo = open('lista de compras.txt', 'a')
arquivo.writelines('==========LISTA DE COMPRAS========== \n')
for a,b in zip(produtos, quantidades):
    print(a, b)
    arquivo.writelines((f'{a}: {b} \n'))