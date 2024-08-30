# O desafio proposto foi para que o usuário pudesse dar entrada em uma string
# e o programa exibisse a string embaralhada. 

from random import sample
info = input("Digite uma palavra: ")
a = sample(info,len(info))
print(a)