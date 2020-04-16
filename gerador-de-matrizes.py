from random import random

tamanho = int(input('Numero de vertices do grafo: '))
nomeArquivo = input('Nome do novo grafo: ')
fator = float(input('Fator de aresta (1 para grafo conectado e 0 para grafo desconectado): '))
#print('Fator de arestas: '+str(fator))

grafo = []
for x in range(tamanho):
    linha=[]
    for y in range(tamanho):
        if x==y:
            linha.append('0')
        elif fator>random():
            linha.append('1')
        else:
            linha.append('0')
    grafo.append(linha)
    
for x in range(tamanho):
    for y in range(tamanho):
        if x!=y:
            grafo[x][y]=(grafo[y][x])[:]


arquivo = open(nomeArquivo,'w')
for x in range(tamanho):
    linha=''
    for y in range(tamanho):
        linha=linha+grafo[x][y]+' '
    arquivo.write(linha[:-1]+'\n')

arquivo.close()
