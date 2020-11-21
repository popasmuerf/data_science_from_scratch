#!/usr/bin/python3



from typing import Any, List, Tuple

A = [[1,2,3],[4,5,6]] # A has 2 rows and 3 columns

B = [[1,2],[3,4],[5,6]] #B has 3 rows and 2 columns


def shape(A:List[List[Any]])->Tuple[int,int]:
    row = len(A)
    columns = len(A[0])
    return (row,columns)

def get_row(A:List[Any],index:int)->List[int]:
    return A[index]

def get_col(A:List[Any],index:int)->List[int]:
    col_vec = list()
    for i in range(len(A)):
        col_vec.append(A[i][index])
    return col_vec

def make_matrix(num_rows:int, num_cols:int, entry_fn):
    '''returns a num_rows x num_cols matrix '''
    ''' whose (i,j)th entry is entry_fn(i,j) '''
    return [[entry_fn(i,j)
      for j in range(num_cols)]
      for i in range(num_rows)]

def is_diagonal(i,j):
    return 1 if i == j else 0



_shapeB:Tuple[int,int] = shape(B)
print(_shapeB)

_shapeA:Tuple[int,int] = shape(A)
print(_shapeA) 

_colA = get_col(A,0)
print(_colA)

_colA = get_col(A,1)
print(_colA)


_colA = get_col(A,2)
print(_colA)

id_matrix = make_matrix(5,5,is_diagonal )
print(id_matrix)