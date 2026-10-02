import pandas as pd

lista_str = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

lista_int = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

val_str = pd.Series(lista_str, index=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'])
val_int = pd.Series(lista_int)

print("Numérico")
print(val_int)
print("----------------")
print("Alfabético")
print(val_str)

print("----------------")
val_int.add(1)

print("Alfabético")
print(val_str.head(6))
print("----------------")
print("Numérico")
print(val_int.tail(7))

print("----------------")
print("Transformação em Dicionário")
val_int = val_int.to_dict()
val_str = val_str.to_dict()

print("----------------")
print("Numérico")
print(val_int)
print("----------------")
print("Alfabético")
print(val_str)