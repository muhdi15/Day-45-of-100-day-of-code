
A = [[5, 0],
     [2, 6]]
print("A", A)

B =[[5, 0, 8],
   [2, 6, 7],
   [1, 3, 4]]
print("B= ", B)

C = [[1, 4, 5, 12],
     [-5, 8, 9, 0],
     [-6, 7, 11, 19]]
print("C = ", C)

#menampilkan nilai pada setiap index

print("matrix A = ")
for index_baris in range (len(A)):
    for index_kolom in range (len(A[index_baris])):
        print(A[index_baris][index_kolom])

print("Matrix B = ")
for index_baris in range (len(B)):
    for index_kolom in range (len(B[index_baris])):
        print(B[index_baris][index_kolom], end='')
    print()

print("Matrix C = ")
for baris in C:
    print(baris)

#Mengakses nilai dalam list

print("C[1]", C[1]) #2nd row
print("C[1][2] = ", C[1][2]) #3rd element of 2nd row
print("C[0][-1] = ", C[0][-1]) #last element of 1st row

column = []; #empty list
for row in C:
    column.append(row[3]) # adds a single item to the existing list
print("3rd column = ", column)


#penjumlahan matriks

mat1 = [[6, 0, 4],
      [2, 7, 3],
      [1, 6, 2]]

mat2 = [[2, 6, 5],
      [3, 2, 4],
      [7, 1, 3]]

result= []
for i in range(len(mat1)):
    row = []
    for j in range(len(mat1[i])):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)

print("The result of adding 2 matrices:")
for row in result:
    print(row)

#perkalian dalam matriks

result = []
for i in range(len(mat1)):
    row = []
    for k in range(len(mat2[0])):
        val = 0
        for j in range(len(mat1[i])):
            val= + mat1[i][j]*mat2[j][k]
        row.append(val)
        result.append(row)

            
print("The result of multiplying 2 matrices: ")
for row in result:
    print(row)




# Buatlah program mencari rata2 dalam matriks tersebut







