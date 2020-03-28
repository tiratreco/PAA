'''
função que lê um arquivo de texto contendo um grafo
deve estar no formato de uma matriz quadrada com zeros e uns
representnado as arestas entre cada vertice
retorna uma matriz quadrada de true/false
'''
def lerGrafo ():
    try:
        arquivo = open('grafo2.txt', 'r')
    except:
        print('Erro de abertura do grafo.')
        return
    grafo = []
    numLinhas = 1
    x = 0
    while x < numLinhas:
        linha = []
        palavra = arquivo.readline()[:-1]
        palavras = palavra.split(' ')
        numLinhas = len(palavras)
        for palavra in palavras:
            linha.append(palavra=='1')
        grafo.append(linha)
        x += 1
    arquivo.close()
    return grafo

'''
função que recebe o grafo no formato descrito e uma lista de inteiros
os inteiros representam os vertices escolhidos
ela avalia se os vertices escolhidos correspondem a um conjunto
de vertices cujos vizinhos e eles próprios sejam todos os vertices do
grafo
retorta true/false
(lembrar que no grafo o vertice 1 corresponde ao indice 0, então
é preciso subtrair 1 a cada vertice da lista a ser verificada)
'''
def visita (grafo, lista):
    visitados = lista.copy()
    for linha in lista:
        for coluna in range(len(grafo)):
            if grafo[linha][coluna] and coluna not in visitados:
                visitados.append(coluna)

    for vertice in range(len(grafo)):
        if vertice not in visitados: return False
    return True
        
    

grafo = lerGrafo()
print (grafo)

verticesEscolhidos = [0 , 3, 1, 2]
visitados = visita(grafo, verticesEscolhidos)

print (verticesEscolhidos)
print (visitados)
