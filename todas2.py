'''
função que calcula todas as combinações de vertices
recebe a quantidade de vertices em cada combinação e a quantidade de vertices do grafo
retorna uma lista de combinações com o tamanho escolhido no parâmetro
nota: se o numero de vertices do grafo passado por parametro for, por exemplo,
10, os vertices serão enumerados de 0 até 9
'''

def combinacoes(num, tam):
    
    combinacoes = []
    
    nums = []
    for i in range(num):
        nums.append(i)
    #nesse ponto nums é a primeira possibilidade
    combinacoes.append(nums[:])
    contador = 1
    #a partir desse ponto nums vai mudando seu valor
    while True:
        cont = 0
        while (nums[num-1-cont]==tam-1-cont):
            cont+=1
        if(cont==num):
            break
        if(cont!=0):
            nums[num-1-cont]+=1
            while (cont!=0):
                cont-=1
                nums[num-1-cont] = nums[num-2-cont]+1
        else:
            nums[num-1+cont]+=1
        
        combinacoes.append(nums[:])
        contador+=1

    print(str(contador)+' combinações calculadas!')
    return combinacoes
    

combinacoes = combinacoes(5, 40)
#print(combinacoes)
