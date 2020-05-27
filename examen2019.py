#ejer5
def maximo_listas(l1,l2,sol):
    print(l1)
    print(l2)
    lonl1 = len(l1)
    lonl2 = len(l2)
    if len(l1) == 1 and len(l2) == 1:
        if l1[0] < l2[0]:
            sol.append(l2[0])
            return sol
        else:
            sol.append(l1[0])
            return sol
    if len(l1) == 1:
        elem = l2[-1:]
        sol = elem + sol
        return maximo_listas(l1, l2[0:lonl1],sol)
    elif len(l2) == 1:
        elem = l1[-1:]
        sol.append(elem)
        return maximo_listas(l1[0:lonl2],l2,sol)
    else:
        elem1 = l1[-1:]
        elem2 = l2[-1:]
        maximo = max(elem1,elem2)
        sol.append(maximo)
        return maximo_listas(l1[0:lonl1],l2[0:lonl2])


def maximasuma(l):
    if len(l) == 1:
        return l[0]
    mitad = len(l)//2
    l1 = l[0:mitad]
    l2 = l[mitad:]
    sol = []
    return maximo_listas(l1,l2, sol)

print(maximasuma([1,2,3]))
