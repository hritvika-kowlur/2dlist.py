List=["orange","grapes","kiwi","watermelon"]

List.append("bannana")

print (List)

del List[0]

print (List)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print (matrix)

print(len(matrix))

for row in range(0,len(matrix)):
    for col in range(0, len(matrix)):
        print (matrix[row][col],end=" ")
        print("\n")


emptymatrix=[]
rows= int(input("Enter the number of rows - "))
cols=int(input("Enter the number of columns - "))

for i in range(rows):
    temp = []
    for j in range(cols):
        x= int(input("Enter your first item "))
        temp.append(x)
    emptymatrix.append(temp)    

for i in range(rows):
    for j in range(cols):
        print(emptymatrix[i][j],end = " ")
    print("\n")            