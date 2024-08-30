# Escreva um programa que calcule o percentual de representação que cada estado
# teve dentro do valor total mensal da distribuidora. O desafio será feito em Python.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
valor_total = (sp + rj + mg + es + outros)
print(f"O valor total do faturamento foi de R${valor_total}.")
print(f"São Paulo teve uma participação de {(sp / valor_total) * 100:.1f}% .")
print(f"Rio de Janeiro teve uma participação de {(rj / valor_total) * 100:.1f}% .")
print(f"Minas Gerais teve uma participação de {(mg / valor_total) * 100:.1f}% .")
print(f"Espírito Santo teve uma participação de {(es / valor_total) * 100:.1f}% .")
print(f"Outros estados tiveram uma participação de {(outros / valor_total) * 100:.1f}% .")
