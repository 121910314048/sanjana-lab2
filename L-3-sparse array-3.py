#promot the user to input values for a matrix ,convert the matrix to a sparse matrix using some threshold value
a=[]
n = int(input("enter number of rows of array : "))
m = int(input("enter number of column of array : "))
for i in range(n):
    b = []
    for j in range(m):
        x = int(input())
        b.append(x)
    a.append(b)
print("Matrix a : ")
for i in a:
    for val in i:
        print(val,end=" ")
    print()
k = int(input("enter the threshold value: "))
for i in range(n):
    for j in range(m):
        if a[i][j]>k:
            a[i][j]=0
print("After conversion : ")
for i in a:
    for val in i:
        print(val,end=" ")
    print()
l =[]
for i in range(n):
    for j in range(m):
        if a[i][j]!=0:
            c = []
            c.append(i)
            c.append(j)
            c.append(a[i][j])
            l.append(c)
print("Sparse matrix :")
for i in l:
    for val in i:
        print(val,end=" ")
    print()

