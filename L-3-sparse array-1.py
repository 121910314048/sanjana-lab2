#Represent a sparse matrix
a = [[1,0,0,0],
     [0,2,0,0],
     [0,0,3,0],
     [0,0,0,4]]
print("Matrix a :")
for i in a:
    for val in i:
        print(val,end=" ")
    print()
b= []
for i in range(4):
    for j in range(4):
        if a[i][j]!=0:
            c = []
            c.append(i)
            c.append(j)
            c.append(a[i][j])
            b.append(c)
print("Sparse matrix :")
for i in b:
    for val in i:
        print(val,end=" ")
    print()        
