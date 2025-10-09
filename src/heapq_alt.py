# Original Code: https://github.com/python/cpython/blob/3.14/Lib/heapq.py

# I'm copying the methods of 'Heapq' instead of importing them because I needed
# to change two lines in order for it to work with my custom heap. I've marked
# these lines with "# original: ...". Other than that, everything works just the
# same as the original heapq sourcecode.

def heapify(x):
    n = len(x)
    for i in reversed(range(n//2)):
        siftup(x, i)

def heappush(heap, item):
    heap.append(item)
    siftdown(heap, 0, len(heap)-1)

def heappop(heap):
    lastelt = heap.pop()
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        siftup(heap, 0)
        return returnitem
    return lastelt

def siftdown(heap, startpos, pos):
    newitem = heap[pos]
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem[0] < parent[0]: # original: if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem

def siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    childpos = 2*pos + 1
    while childpos < endpos:
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos][0] < heap[rightpos][0]: # original: if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    heap[pos] = newitem
    siftdown(heap, startpos, pos)
