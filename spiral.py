def createMatrix(S):
    lst = []
    for i in range(1, (S*S)+1):
        lst.append(i)

    Matrix = []
    while lst != []:
        Matrix.append(lst[:S])
        lst = lst[S:]
    return Matrix

def findSpinend(S):
    r = 0
    if S%2 == 0:
        r = int(S/2)
        return r+1, r
    else:
        r = int((S+1)/2)
        
        return r , r
    
def throuprow(S):
    cord = []
    for i in range(S-1):
        cord.append([0, i])
    return cord

def throdowncol(S):
    cord = []
    for i in range(S-1):
        cord.append([i, S-1])
    return cord

def throdownrow(S):
    cord = []
    for i in range(S-1, 0, -1):
        cord.append([S-1, i])
    return cord

def throupcol(S):
    cord = []
    for i in range(S-1, 0, -1):
        cord.append([i, 0])
    return cord

printedele = []
def eleprint(ele, Matrix):
    for i in ele:
        #print(i)
        print(Matrix[i[0]][i[1]], end=' ')
        printedele.append(Matrix[i[0]][i[1]])


def removeitems(lst, Matrix, index):
    for j in lst:
        #print(lst)
        for i in range(index):
            if j in Matrix[i]:
                Matrix[i].remove(j)

    Matrix.pop(0)
    Matrix.pop(len(Matrix)-1)
    #print(Matrix)
    return Matrix
        

index = int(input("Enter matrix Size: "))
mat = createMatrix(index)
for i in range(len(mat)):
    print(mat[i])
#print(mat)
m, n = findSpinend(index)
print('End cooridinates are: ({}, {})'.format(m, n))
print('Matrix is of size: ({}, {})'.format(index, index))
while index>1:
    ele = throuprow(index)
    eleprint(ele, mat)

    ele = throdowncol(index)
    eleprint(ele, mat)

    ele = throdownrow(index)
    eleprint(ele, mat)

    ele = throupcol(index)
    eleprint(ele, mat)

    mat = removeitems(printedele, mat, index)
    printedele = []
    index -= 2
    if index==1:
        print(mat[0][0])
