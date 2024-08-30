# O desafio proposto foi para criar e printar a sequencia de fibonacci, onde o usuário
# poderia escolher um número e verificar se o mesmo se encontra na sequência. 

n = int(input("Digite um número inteiro: "))
n2 = n + 1
t1 = 0
t2 = 1
t3 = t1 + t2
print(f"\n{t1}", end=" - ")

while t3 < n2:
    print(f"{t3}", end=" - ")
    t3 = t1 + t2
    t1 = t2
    t2 = t3

print("FIM")


if (n == t1):
    print("\nO valor informado se encontra na sequência de Fibonacci.")
else:
    print("\nO valor informado não se encontra na sequência de Fibonacci.")
