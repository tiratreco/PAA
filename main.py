import networkx as nx
import matplotlib.pyplot as plt
import sys


def find_ccdm(G):
    '''
    Encontra o CONJUNTO CONECTADO DOMINANTE MÍNIMO
    '''
    adjacencia = {}
    for i in G.adj:
        lista  = list(G[i])
        lista.append(i)
        adjacencia.update({i: lista})

    transmissores = {}
    
    for i in adjacencia: 
       # print("Transmissores:",transmissores)
        for j in list(transmissores.keys()): 
                #Se esse vertice tiver mais conexões e se o já adicionado na lista está contido nele((ou seja, tem todas suas conexoes)
                if len(adjacencia[i]) > len(adjacencia[j]) and set(adjacencia[j]).intersection(adjacencia[i]) == set(adjacencia[j]):
                    #Se sim, remove o antigo e insere o atual
                    #print("Troca:",i,j)
                    transmissores.pop(j)
                    transmissores.update({i:adjacencia[i]})
        
        #se esse tem algum vertice que não pode ser visitado pelos transmissores
        if set(adjacencia[i]).difference(Conjunto_Visitado(transmissores,adjacencia) ):
            #ele é adicionado na lista de transmissores
            transmissores.update({i:adjacencia[i]})
           
    for i in transmissores:
        print(i,end=", ")

    return transmissores




   
def Conjunto_Visitado(transmissores,grafo):
    conjunto = []
    for i in transmissores:
        for j in grafo[i]:
            if j not in conjunto:    conjunto.append(j)
            
    return conjunto
                

n= param  = sys.argv[1] #recebe número de vertices
n = int(n)
arq = open('grafo'+str(n) +'.txt', 'r')
matriz_adjacencia = []
G = nx.Graph()
converte_int = lambda a : int(a)

for i in arq: 
    vertices_string = i.split(" ")
    vertices_int = list(map(converte_int,vertices_string))
    matriz_adjacencia.append(vertices_int)

for i in range(n):
    G.add_node(i)

for i in range(n):
    for v in range(len(matriz_adjacencia[i])):
        if i == v: pass
        if(matriz_adjacencia[i][v] == 1):
            G.add_edge(i,v)

transmissores =find_ccdm(G)

pos = nx.kamada_kawai_layout(G)
cores = ["blue"] * (n)

for i in transmissores:
    cores[i] = 'red'

nodes = nx.draw_networkx_nodes(G, pos, node_size=130, node_color=cores, ) #desenhando nodes
label = nx.draw_networkx_labels(G, pos, font_size=8, font_family="Arial", font_color='white')#desenhando nomes/labes nos nodes
edges = nx.draw_networkx_edges(G, pos, width=1)#desenhando arestas
ax = plt.gca()
#ax.plot([0],[0],color="blue",label="Não vão retransmitir")
#ax.plot([0],[0],color="red",label="Retransmissores")
import matplotlib.patches as mpatches
red = mpatches.Patch(color='red', label='Retransmissores')
blue =  mpatches.Patch(color='blue', label='Não vão retransmitir')

plt.legend(handles=[red,blue])

plt.savefig("Grafo"+str(n) +"_Conjunto_Dominante.png", format="PNG") #salvando grafo
plt.show()

 



                