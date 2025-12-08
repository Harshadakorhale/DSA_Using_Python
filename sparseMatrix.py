matrix = [
    [0,0,3,0,4],
    [0,0,5,7,0],
    [0,0,0,0,0],
    [0,2,6,0,0]
]
sparse =[]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j]!=0:
            sparse.append([i,j,matrix[i][j]])
    print("Row column value")
    for row in sparse:
        print(row)