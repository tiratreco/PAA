import matplotlib.patches as mpatches
import networkx as nx
import matplotlib.pyplot as plt

import sys
import time


'''
função que lê um arquivo de texto contendo um grafo
deve estar no formato de uma matriz quadrada com zeros e uns
representnado as arestas entre cada vertice
retorna uma matriz quadrada de true/false
'''


def lerGrafo():
    nomeArquivo = input(str('Nome do arquivo: '))
    try:
        arquivo = open(nomeArquivo, 'r')
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
            linha.append(palavra == '1')
        grafo.append(linha)
        x += 1
    arquivo.close()
    return grafo, nomeArquivo


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


def visita(grafo, lista):
    visitados = lista.copy()
    for linha in lista:
        for coluna in range(len(grafo)):
            if grafo[linha][coluna] and coluna not in visitados:
                visitados.append(coluna)

    for vertice in range(len(grafo)):
        if vertice not in visitados:
            return False
    return True


'''
função que calcula todas as combinações de vertices
recebe a quantidade de vertices em cada combinação e a quantidade de vertices do grafo
retorna uma lista de combinações com o tamanho escolhido no parâmetro
nota: se o numero de vertices do grafo passado por parametro for, por exemplo,
10, os vertices serão enumerados de 0 até 9
retorna n!/(p!(n-p)!) combinações
'''
def combinacoes(num, tam):
    combinacoes = []
    nums = []
    for i in range(num):
        nums.append(i)
    # nesse ponto nums é a primeira possibilidade
    combinacoes.append(nums[:])
    contador = 1
    # a partir desse ponto nums vai mudando seu valor
    while True:
        cont = 0
        while (nums[num-1-cont] == tam-1-cont):
            cont += 1
        if(cont == num):
            break
        if(cont != 0):
            nums[num-1-cont] += 1
            while (cont != 0):
                cont -= 1
                nums[num-1-cont] = nums[num-2-cont]+1
        else:
            nums[num-1+cont] += 1
        combinacoes.append(nums[:])
        contador += 1
    print(str(contador)+' combinações calculadas!')
    return combinacoes


def forcaBruta(grafo):
    for cont in range(len(grafo)):
        conjuntos = combinacoes(cont+1, len(grafo))
        for combinacao in conjuntos:
            if visita(grafo, combinacao):
                print('Combinação de vertice(s) que cobre o grafo encontrada!')
                return combinacao
        print('Nenhuma cobertura formada por ' +
              str(cont+1)+' vertice(s) encontrada.')
    print('Nenhuma combinação de vertice(s) que cobre o grafo encontrada!')


def salvarImagem(grafo, resposta, nomeArquivo):
    G = nx.Graph()
    for v in range(len(grafo[0])):
        G.add_node(v)
    for i in range(len(grafo)):
        for v in range(len(grafo[i])):
            if i != v and (grafo[i][v] == 1):
                G.add_edge(i, v)
    pos = nx.kamada_kawai_layout(G)
    cores = ["blue"] * (len(grafo))
    for v in resposta:
        cores[v] = 'red'
    nodes = nx.draw_networkx_nodes(
        G, pos, node_size=130, node_color=cores, )  # desenhando nodes
    # desenhando nomes/labes nos nodes
    label = nx.draw_networkx_labels(G, pos, font_size=8, font_color='white')
    edges = nx.draw_networkx_edges(G, pos, width=1)  # desenhando arestas
    red = mpatches.Patch(color='red', label='Retransmissores')
    blue = mpatches.Patch(color='blue', label='Não vão retransmitir')
    plt.legend(handles=[red, blue])
    plt.savefig(nomeArquivo[:-4]+"_Conjunto_Dominante.png",
                format="PNG")  # salvando grafo


grafo, nomeArquivo = lerGrafo()
start_time = time.time()
resposta = forcaBruta(grafo)
print(resposta)
print("--- %s seconds ---" % (time.time() - start_time))
salvarImagem(grafo, resposta, nomeArquivo)
