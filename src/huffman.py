from src.heapq_alt import heapify, heappush, heappop


def char_count(text):
    count = []
    for character in set(text):
        count.append((text.count(character), character))
    return count # Lista de tuplas com a contagem e o caracter

def prefix_tree(count):
    heapify(count)
    while(len(count)>1):
        value_0 = heappop(count)
        value_1 = heappop(count)
        x = value_0[0] + value_1[0]
        y = [value_0[1], value_1[1]]
        value = (x, y)
        heappush(count, value)
    return count[0][1]

def prefix_codes(tree):
    pass