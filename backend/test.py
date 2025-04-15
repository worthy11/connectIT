class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class B:
    def __init__(self, lista):
        self.lista = list(lista)

a1 = A("a1", "b1")
a2 = A("a2", "b2")
l1 = [a1, a2]
b1 = B(l1)
for a in b1.lista:
    print(a.a, a.b)

l2 = [a1]
b2 = B(l2)
l1[0] = "change"
for a in b1.lista:
    print(a.a, a.b)
for a in b2.lista:
    print(a.a, a.b)