# Gera uma lista com a contagem de cada caracter na string
def char_count(text):
    count = [] # Lista para armazenar as contagens

    for char in set(text): # Obs: cada execução do set gera um "count" em ordem diferente
        count.append((text.count(char), char)) # Adiciona uma tupla com o caracter e sua contagem

    return count # Lista de tuplas contendo o caracter e a sua contagem


# Gera uma árvore de prefixos, representada por vetores
def prefix_tree(count):
    if(len(count) <= 1):
        return (0, []) if len(count)==0 else (count[0][0], [count[0][1]]) # Excessões: número de chars é 0 ou 1

    while(len(count) > 1): # Loop: junta os nós em árvores até formar uma única árvore
        count.sort(key=lambda h: h[0]) # Ordena os elementos (listas/nós ou chars/folhas) por frequência
        x, y = count.pop(0), count.pop(0) # Remove os 2 elementos com a menor frequência 

        value = (x[0] + y[0], [x[1], y[1]]) # Soma as frequências e liga os dois elementos a um nó
        count.append(value) # Adiciona a nova árvore à lista

    return count[0] # Tupla: contagem de elementos + esquema de vetores representando a árvore de prefixos


# Gera um dicionário contendo os prefix code de cada caracter
def prefix_codes(tree):
    stack = [('0', tree)] if len(tree) else [] # Pilha para percurso na árvore
    codes = {} # Dicionário {caractere: prefixo}

    while(len(stack) > 0):
        if(type(stack[-1][1]) != list): # Se for uma string (folha da árvore)
           codes[stack[-1][1]] = stack[-1][0][1:] # Salva no dicionário
           stack.pop(-1) # Remove da pilha
        elif(len(stack[-1][1]) == 2): # Se tiver 2 filhos
            parent = stack.pop(-1) # Remove o pai da pilha
            stack.append((parent[0]+'1', parent[1][1])) # Desembrulha o filho dir
            stack.append((parent[0]+'0', parent[1][0])) # Desembrulha o filho esq
        elif(len(stack[-1][1]) == 1): # Se tiver 1 filho
            stack[-1] = (stack[-1][0]+'0', stack[-1][1][0]) # Desembrulha o único filho (esq)

    return codes # Dicionário com os caracteres (keys) e seus prefixos (values)