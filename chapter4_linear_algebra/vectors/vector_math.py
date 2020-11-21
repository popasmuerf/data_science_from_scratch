#!/usr/bin/python3
import math
from typing import List


height_weight_age = [70,
                     170,
                     40]


grades = [95,
          80,
          75,
          62]


v1:List[float] = list()
v2:List[float] = list()
v3:List[float] = list()
v4:List[float] = list()

for i in range(20):
    v1.append(i)
    v2.append(i *(-1) )
    v3.append(i)
    v4.append(i *(-1) )



def add_vectors(*argv):
    vector = list()
    max = len(argv[0])
    for k in range(max):
        vector.append(0)
    max = len(argv)
    for i in range(max):
        for j in range(len(argv[i])):
            vector[j] = (vector[j] + argv[i][j])
    return vector

def add_vectors_list(arg_list):
    vector = list()
    max = len(arg_list[0])
    for k in range(max):
        vector.append(0)
    max = len(arg_list)
    for i in range(max):
        for j in range(len(arg_list[i])):
            vector[j] = (vector[j] + arg_list[i][j])
    return vector


def sum_of_squares(v):
    ''' v_1 * v_1 + ... + v_n * v_n '''
    return dot_product(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def squared_distance(v,w):
    """(v_1 - w_1) ** 2 + ... + (v_n - w_n) ** 2 """
    return sum_of_squares(sub_vectors(v,w))

def distance(v,w):
    return math.sqrt(squared_distance(v,w))

def sub_vectors(*argv):
    vector = list()
    max = len(argv[0])
    for k in range(max):
        vector.append(0)
    max = len(argv)
    for i in range(max):
        for j in range(len(argv[i])):
            vector[j] = (vector[j] - argv[i][j])
    return vector

def mult_by_scalar(scalar,vector):
    rvector = list()
    max = len(vector)
    for k in range(max):
        rvector.append(0)
    max = len(vector)
    for j in range(len(vector)):
        rvector[j] = (vector[j] * scalar )
    return rvector


def vector_mean(vector_list):
    n = len(vector_list)
    rvector = mult_by_scalar(1/n, add_vectors_list(vector_list))
    return rvector

def dot_product(v,w):
    '''v_1 * w_1 + .... + v_n * w_n '''
    return sum(v_i * w_i for v_i, w_i in  zip(v,w))


foo = add_vectors(v1,v2,v3)
print(foo)

bar = sub_vectors(v1,v2,v3,v4)
print(bar)

foobar = mult_by_scalar(5,v1)
print(foobar)

alpha = vector_mean([v1,v2])
print(alpha)

beta = dot_product(v1,v2)
print(beta)