
def dot (a,b):
    dotproduct=0
    for a,b in zip(a,b):
        dotproduct = dotproduct+a*b
    return dotproduct

def cross(a, b):
    c = [a[1]*b[2] - a[2]*b[1],
         a[2]*b[0] - a[0]*b[2],
         a[0]*b[1] - a[1]*b[0]]

    return c


def mul(X,Y):
    result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
    return result

def zeros_matrix(rows, cols):

    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)
 
    return M
def copy_matrix(M):

    rows = len(M)
    cols = len(M[0])
 
    MC = zeros_matrix(rows, cols)
 
    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]
 
    return MC
def norm(a):
    mb=0
    for i in range(len(a)):
        mb+=a[i]**2
    module= mb**0.5
    r=[]
    for i in range(len(a)):
        r.append(a[i]/module)
    return r

    return new

def subtract(matrix1, matrix2):
#     matrix1Rows = len(matrix1)
#     matrix2Rows = len(matrix2)
#     matrix1Col = len(matrix1[0])
#     matrix2Col = len(matrix2[0])
# 
#     #base case
#     if(matrix1Rows != matrix2Rows or matrix1Col != matrix2Col):
#         return "ERROR: dimensions of the two arrays must be the same"

    #make a matrix of the same size as matrix 1 and matrix 2
    matrix = []
    rows = []

    for i in range(0, matrix1Rows):
        for j in range(0, matrix2Col):
            rows.append(0)
        matrix.append(rows.copy())
        rows = []

    #loop through the two matricies and the subtraction should be placed in the
    #matrix
    for i in range(0, matrix1Rows):
        for j in range(0, matrix2Col):
            matrix[i][j] = matrix1[i][j] - matrix2[i][j]
            
    return matrix





def eliminate(r1, r2, col, target=0):
    fac = (r2[col]-target) / r1[col]
    for i in range(len(r2)):
        r2[i] -= fac * r1[i]

def gauss(a):
    for i in range(len(a)):
        if a[i][i] == 0:
            for j in range(i+1, len(a)):
                if a[i][j] != 0:
                    a[i], a[j] = a[j], a[i]
                    break
            else:
                raise ValueError("Matrix is not invertible")
        for j in range(i+1, len(a)):
            eliminate(a[i], a[j], i)
    for i in range(len(a)-1, -1, -1):
        for j in range(i-1, -1, -1):
            eliminate(a[i], a[j], i)
    for i in range(len(a)):
        eliminate(a[i], a[i], i, target=1)
    return a

def inverse(a):
    tmp = [[] for _ in a]
    for i,row in enumerate(a):
        assert len(row) == len(a)
        tmp[i].extend(row + [0]*i + [1] + [0]*(len(a)-i-1))
    gauss(tmp)
    ret = []
    for i in range(len(tmp)):
        ret.append(tmp[i][len(tmp[i])//2:])
    return ret


