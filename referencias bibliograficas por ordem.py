# coding: utf-8
#
# Anderson Sales

def quicksort(v):
    if len(v) <= 1:
        return v # uma lista vazia ou com 1 elemento ja esta ordenada
    less, equal, greater = [], [], [] # cria as sublistas dos maiores, menores e iguais ao pivo
    pivot = v[0][:] # escolhe o pivo. neste caso, o primeiro elemento da lista
    for x in v:
# adiciona o elemento x a lista correspondeste
        if x[:] < pivot:
            less.append(x)
        elif x[:] == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return quicksort(less) + equal + quicksort(greater)


f = open('ref.txt', 'r')
texto = f.read()
f.close()

refs = texto.split("*")

refs = quicksort(refs)

final = ""
count = 0
for ref in refs:
    final += ref
    count+=1

print count
f = open('res.txt', 'w')
f.write(final)
f.close()