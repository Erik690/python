pismena = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
cisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
znaky = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print("Pismena: ", pismena)
# print("Cisla: ", cisla)
# print("Znaky: ", znaky) 
# print("Matrix: ", matrix)
# print("Pismena[2]: ", pismena[2])
# print("Cisla[4]: ", cisla[4])
# print("Znaky[6]: ", znaky[6])
# print("Matrix[1][2]: ", matrix[1][2])
# print("Pismena[2]: ", pismena[:2])
# print("Cisla[4]: ", cisla[:4])
# print("Znaky[6]: ", znaky[:6])
# print("Matrix[1][2]: ", matrix[1][:2])
# print("Pismena[2]: ", pismena[2:])
# print("Cisla[4]: ", cisla[4:])
# print("Znaky[6]: ", znaky[6:])
# print("Matrix[1][2]: ", matrix[1][2:])

first, second, *other = cisla
print (first)
print (other)