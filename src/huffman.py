from heapq_alt import heapify, heappush, heappop


def char_count(text):
    count = []
    for character in set(text):
        count.append((text.count(character), character))
    return count # Lista de tuplas com a contagem e o caracter

def prefix_tree(count):
    heapify(count)
    while(len(count)>1):
        x = heappop(count)
        y = heappop(count)
        value = (x[0] + y[0], [x[1], y[1]])
        heappush(count, value)
    return count[0][1] # Esquema de vetores representando a árvore de prefixos

def prefix_codes(tree):
    codes, prefix = {}, ''
    tree = [tree]
    current_branch = tree

    while tree != [None]:
        #print(f'>>> {codes} // {prefix} // {tree}')

        if(current_branch[0] != None):
            n = 0
        elif(current_branch[-1] != None):
            n = 1
        else:
            current_branch = tree
            for c in prefix[:-1]:
                current_branch = current_branch[int(c)]
            current_branch[int(prefix[-1])] = None
            prefix = prefix[:-1]
            continue

        if(type(current_branch[n]) == list):
            prefix += f'{n}'
            current_branch = current_branch[n]
        elif(type(current_branch[n]) == str):
            binary = prefix + str(n)
            codes[current_branch[n]] = binary[1:]
            current_branch[n] = None
    return codes

