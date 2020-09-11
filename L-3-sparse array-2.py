#Represent a sparse matrix using user define function
def display(x):
    for i in x:
        for val in i:
            print(val,end=" ")
        print()
def convert(x):
    b= []
    for i in range(4):
        for j in range(4):
            if x[i][j]!=0:
                c = []
                c.append(i)
                c.append(j)
                c.append(a[i][j])
                b.append(c)
    print("Sparse matrix :")
    display(b)
a = [[1,0,0,0],
     [0,2,0,0],
     [0,0,3,0],
     [0,0,0,4]]
print("Matrix a :")
display(a)
convert(a)
