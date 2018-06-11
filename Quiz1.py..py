# matvec takes a matrix and a vector and returns a corresponding matrix-vector multiple 
def matvec(matrix,vector):
    """
This function takes an empty list.
Takes a matrix and a vector as arguments.
Updates the matrix and the vector.
It then appends to empty list titled result.
Then returns updated list titled result.
    """
    result=[]
    for i in range(len(matrix)):
        total = 0
        for j in range(len(vector)):
            total += matrix[i][j]*vector[j]
        result.append(total)
    return result

# These are test variables to test the function matvec

matrix1=[[2,-1],[1,1]]
vector1=[1,2]

matrix2=[[3,3],[1,1]]
vector2=[1,2]

matrix3=[[3,3,3],[4,4,4]]
vector3=[1,2,3]

# They should be tested one at a time

print(matvec(matrix1,vector1))
#print(matvec(matrix1,vector1))
#print(matvec(matrix1,vector1))


















"""def matvec(matrix,vector):
    result=[]
    for i in range(len(matrix)):
        total = 0
        for j in range(len(vector)):
            total += matrix[i][j]*vector[j]
        result.append(total)
    return result
matrix=[[2,-1],[1,1]]
vector=[1,2]
print(matvec(matrix,vector))"""
    











 
                                 
        
