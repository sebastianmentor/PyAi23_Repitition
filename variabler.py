
# En variabel är då endast ett namn som 'innehåller' data eller vet vart data är lokaliserad!!

import math

variabel_1:int = 109

var1, var2, var3 = (1,2,3)
print(f'{var1}')
var1, var2, var3 = ['var1','var2','var3']

print(f'{var1=}')
print(f'{var2=}')

var1, var2 = var2 , var1

print(f'{var1=}')
print(f'{var2=}')

print(type(int))
print(type(45))
print(type(math))

del var1
# print(var1)

seriefigur = 'Kalle'

min_ålder = 10
print(id(min_ålder))
någon_annans_ålder = min_ålder
print(id(någon_annans_ålder))

min_ålder = 11

print(min_ålder)
print(någon_annans_ålder)
print(id(min_ålder))
print(id(någon_annans_ålder))


my_list = [1,2,'hej']
print(id(my_list))

same_list = my_list
print(id(same_list))

my_list.append('22')

print(my_list, same_list)

