# En ordnad mängd data

min_lista = [1,2,3,'datatyper', 2.33]

min_lista.append(min_lista)

print(min_lista)

print(min_lista[-1])

listor_i_lista = [[1,2],[3,4]]

print(listor_i_lista)

print(listor_i_lista[0][1])
listor_i_lista[0][1] = 5
print(listor_i_lista)
print(listor_i_lista[0][1])

new_list = listor_i_lista[0] + listor_i_lista[1] + listor_i_lista
print(new_list)

new_list = new_list * 3

print(new_list)

dålig_lista = 4*[[]]

# for lista in dålig_lista:
#     print(id(lista))

dålig_lista[0].append(8)

print(dålig_lista)

min_lista.extend(['a','b','c'])

print(min_lista)

print(min_lista.index('b'))

print(min_lista.reverse())
print(min_lista)

my_tuple = (min_lista, 'hej', 12)
print(my_tuple)
min_lista.reverse()
print(my_tuple)

my_tuple[0].reverse()
# my_tuple[0].sort()

MIN_TUPLE = (1,2,3,4,5)

# min_tuple[2] = 11

# bad practice!!!!
MIN_TUPLE = MIN_TUPLE + (6,7)
print(MIN_TUPLE)