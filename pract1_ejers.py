def ejer1(n):
    if n == 1:
        return 1
    else:
        return (2 * n - 1) + ejer1(n - 1)


print(ejer1(2))


def ejer2(n):
    if n < 10:
        return 1
    else:
        return 1 + ejer2(n // 10)


print(ejer2(100))


def ejer3(x, d):
    if len(d) == 1:
        return d[0]
    else:
        aux = d[0]
        d.pop(0)
        return aux + x * ejer3(x, d)


print(ejer3(3, [1, 2, 3, 4]))

def ejer4_1(n):
    if n == 1:
        return 1
    else:
        return ejer4(n) + ejer4_1(n - 1)


def ejer4(n):
    if n < 3:
        return 1
    else:
        return 1 + ejer4_1(n - 2)


print(ejer4(3))

def ejer6(x,a):
    b = []
    if len(a)<1:
        return a.append(x)
    else:
        return ejer6aux(x,a,b)

def ejer6aux(x,a,b):
    if a[0]<= x:
        b.append(a[0])
        a.pop(0)
        return ejer6aux(x,a,b)
    else:
        b.append(x)
        b.extend(a)
        return b

print(ejer6(5, [4,9,11]))

"""def ejer7(a):
    n = len(a)
    if n==0:
        return a
    else:
        return ejer6(a[n-1],(ejer7(a[0:n-1])))

print(ejer7([7,5,4]))


def ejer8(n):
    if n == 1:
        print("Muevo disco"+ n + "de torre de a a b")
        print("Muevo disco"+ n + "de torre de b a c")
    else:
        return ejer8(n-1)
        print("Muevo disco" + n + "de torre de a a b")
        return ejer8(n-1)
        print("Muevo disco"+ n + "de torre de b a c")
        return ejer8(n-1)

ejer8(2)"""

def ejer9(x,a):
    inf=0
    return ejer9_1(x,a,inf, len(a)-1)

def ejer9_1(x,a,inf, sup):
        mitad = (inf + sup)//2
        if inf>sup:
            return -1
        else:
            if a[mitad] == x:
                return mitad
            elif x<a[mitad]:
                return ejer9_1(x,a,0,mitad-1)
            else:
                return ejer9_1(x,a,mitad+1,sup)

print(ejer9(5, [1,2,3,4,5]))

def ejer8(piezas, izda, centro, derecha):
    if piezas==1:
        print("Muevo pieza " + str(piezas) + " de " + izda + " a " + centro)
        print("Muevo pieza " + str(piezas) + " de " + centro + " a " + derecha)
    else:
        ejer8(piezas - 1, izda, centro, derecha);
        print("Muevo pieza " + str(piezas) + " de " + izda + " a " + centro);
        ejer8(piezas - 1, derecha, centro, izda);
        print("Muevo pieza " + str(piezas) + " de " + centro + " a " + derecha)
        ejer8(piezas - 1, izda, centro, derecha);


print(ejer8(2,"1","2","3"))

def fx(x, a):
    return x**2 - a

def der(x):
    return 2*x

def siguiente(x, a):
    next = x - (fx(x,a)//der(x))
    return ejer5(x, next)

def ejer5(x, a):
    if abs(a) < 0.000001:
        return a
    else:
        return siguiente(x, a)

def auxinsert(x,a,n):
    if a[0]>x:
        a.insert(0,x)
        return a
    elif a[n] < x:
        a.insert(n+1, x)
        return a
    else:
        n= n-1
        return auxinsert(x,a,n-1)

def insertelem(x,a):
    n = len(a)
    if n==0:
        a.append(x)
        return a
    else:
        n = n-1
        return auxinsert(x,a,n)

print(insertelem(1, [10]))

def insertsort(a):
    n = len(a)
    if n<1:
        return a
    else:
        elem = a[n-1]
        n = n-1
        return insertelem(elem,insertsort(a[0:n]))

print (insertsort([7,3,1,9,15]))
