#write a python programme to find operations and linear algebraic operations of two 3x3 matrices by using numpy
#operations on matrices
import numpy as np
n1=np.array([input("enter first 3x3 matrix\n")])
print n1
n2=np.array([input("enter second 3x3 matrix\n")])
print n2
a=np.add(n1,n2)
print"adition of matrix is\n",a
c=np.dot(n1,n2)
print"dot multiplication of matrices is\n ",c
d=np.cross(n1,n2)
print "cross product of matrices is \n",d
e=np.transpose(n1)
print"transpose of matrix 1 is\n",e
f=np.transpose(n2)
print "transpose of matrix 2 is\n",f
b=np.trace(n1)
print "trace of matrix 1\n",b
n=np.trace(n2)
print "trace of matrix 2 is\n",n
#linear algebraic operations of matrices
g=np.linalg.matrix_rank(n1)
h=np.linalg.matrix_rank(n2)
print "\nrank of matrices are\n",g,h
i=np.linalg.det(n1)
j=np.linalg.det(n2)
print "\ndeterminants of matrices are\n",i,j
k=np.linalg.inv(n1)
print "\ninverse of matrix 1 is\n",k
l=np.linalg.inv(n2)
print "inverse of matrix 2 is\n",l
m=np.linalg.eigh(n1)
print "eighen value of matrix 1 is\n",m
o=np.linalg.eigh(n2)
print "eighen values of matrix 2 is\n",o



