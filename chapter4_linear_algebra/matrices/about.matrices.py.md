#Matrices 

A matrix is a two-dimensional collection of numbers(a 1-dimentional
matrix is just a vector...).

We can represent matrices as lists of lists, with each inner
list having the same size and representing a **row** of the
matrix.  If **A** is a matrix, then  **A**[i][j]  is th eelement in 
the **i**th row and the **j**th column.

Per mathematical convention...you should try to use capital letters to
represent matrices..For Example:

A = [[1,2,3],[4,5,6]] # A has 2 rows and 3 columns

B = [[1,2],[3,4],[5,6]] #B has 3 rows and 2 columns


In Python and most other programming languages...we have to be carefule
to remember that "row 1" here in implementation is actually "row 0"...
so always keep in mind there is a going to be a an offset of +1 when
dealing with lists or arrays....

If a matrix has **n** rows and **k** columns, we 
will refer to it as  a  **n x k** matrix.  We can 
(and sometimes will) think of each row of a **n x k**
matrix as a vector of length **k**, and each column
as a vecotr of length **n** :


## Why are matrices important ?
Matrices are important to us for severa reasons...
First, we can use a matrix to represent a data set
consisting of multiple vectors, simply by considering
each vector as a row of the matrix.  

For example, if you had the heights, wieghts,and ages
of 1,000 people you could put them in a
1,000 x3  matrix:

We can also...which is perhaps a matrix'
most powerful attribute...is that we can
use an **n** x **k** matrix to represent 
a liniear function that maps **k**-dimensional vectors
to **n**-dimensional vecotrs.

Third...matrices can be used to represent binary
relations instead of having a single list
of a bunch of tuples representing graph edges....
we could represent connections in a matrix...

from this....

        friendships = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4)]


to this....

friendshps = [[0,1,1,0,0,0,0,0,0], #user0
              [1,0,1,1,0,0,0,0,0], #user1
              [1,1,0,0,0,0,0,0,0], #user2
              [1,1,0,1,0,0,0,0,0], #user3
              [0,1,1,0,1,0,0,0,0], #user4
              [0,0,0,1,0,1,0,0,0], #user5
              [0,0,0,0,1,0,0,1,0], #user6
              [0,0,0,0,1,0,0,1,0], #user7
              [0,0,0,0,0,1,1,0.1]] #user8

There are some trade offs here...
If there are very few connections...there could be an argument
for  this data structure being a waste of resources...
...however a counter arugment can be made that the resources
used to generate this data structure is more than made up for
for the O(1) time to access for any known connection for any
user.....or trying to figure out if there is a connection 
and to whom.....

friendships[0][2] == 1 
friendships[0][8] == 1


All of the machinary here we built by hand is also 
available via NumPy

