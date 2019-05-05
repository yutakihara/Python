#
# Name: Yuta Kihara
# Description of program:
# Python lists and the def keyword to create five functions that work on 1D and 2D lists.
# 1.Computing the Prefix Sum
# 2.Returning Diagonal of a Matrix (2D List)
# 3.Checking if Matrix (2D List) is Symmetry
# 4.Returning Transpose of a Matrix (2D List)
# 5.Adding Two Matrices (2D Lists)
# Python, a matrix can be created using 2D lists, also called a two-dimensional table.
#

# 1.Computing the Prefix Sum
def prefix＿sum(one_dim_list):
    prefix_sum_list = []
    sum = 0
    for position in range(len(one_dim_list)):
        sum += one_dim_list[position]
        prefix_sum_list.append(sum)
    return prefix_sum_list

# 2.Returning Diagonal of a Matrix (2D List)
def diagonal(matrix):
    diagonal_list = []
    for row in range(len(matrix)):
        col = row
        diagonal_list.append(matrix[row][col])
    return diagonal_list

# 3.Checking if Matrix (2D List) is Symmetry
def symmetric(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if(matrix[row][col] != matrix[col][row]):
                return False
    return True

# 4.Returning Transpose of a Matrix (2D List)
def transpose(matrix):
    transpose_matrix = []
    col = 0
    while(col < len(matrix[0])):
        temp = []
        for row in range(len(matrix)):
            temp.append(matrix[row][col])
        transpose_matrix.append(temp)
        col+=1
    return transpose_matrix

# 5.Adding Two Matrices (2D Lists)
def addition(matrix1,matrix2):
    addition_matrix = []
    for row in range(len(matrix1)):
        temp = []
        for col in range(len(matrix1[row])):
            temp.append(matrix1[row][col] + matrix2[row][col])
        addition_matrix.append(temp)
    return addition_matrix
