# Gera uma lista com a contagem de cada caracter na string
def char_count(text):
    count = []
    for character in set(text): # Obs: cada execução do set gera um "count" em ordem diferente
        count.append((text.count(character), character))

    return [(count[0][0], [count[0][1]])] if len(count) == 1 else count # Lista de tuplas com a contagem e o caracter


# Gera uma árvore de prefixos, representada por vetores
def prefix_tree(count):
    while(len(count)>1):
        count.sort(key=lambda h: h[0])
        x, y = count.pop(0), count.pop(0)

        value = (x[0] + y[0], [x[1], y[1]])
        count.append(value)

    return count[0] if len(count) else (0, []) # Esquema de vetores representando a árvore de prefixos + contagem de caracteres


# Gera um dicionário contendo os prefix code de cada caracter
def prefix_codes(tree):
    stack = [('0', tree)] if len(tree) else []
    codes = {}

    while(len(stack) > 0):
        #print(f'>>> {codes} // {stack}') # Debug
        if(type(stack[-1][1]) != list): # Se for uma string (folha da árvore)
           codes[stack[-1][1]] = stack[-1][0][1:]
           stack.pop(-1)
        elif(len(stack[-1][1]) == 2): # Se tiver 2 filhos
            parent = stack.pop(-1)
            stack.append((parent[0]+'1', parent[1][1]))
            stack.append((parent[0]+'0', parent[1][0]))
        elif(len(stack[-1][1]) == 1):  # Se tiver 1 filho
            stack[-1] = (stack[-1][0]+'0', stack[-1][1][0])

    return codes # Dicionário com os caracteres (keys) e seus prefixos (values)
