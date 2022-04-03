import sympy as s
from sympy.matrices import Matrix

def DistanceMatrix(d):
    return Matrix([[1, d], [0, 1]])

def RefractionMatrix(R, n1, n2):
    return Matrix([[1, 0], [(1/R)*((n1/n2)-1), (n1/n2)]])

def ThickLens(R1, R2, n1, n2, d):
    return (RefractionMatrix(R2, n2, n1) * DistanceMatrix(d) * RefractionMatrix(R1, n1, n2) )

def ThinLens(f):
    return Matrix([[1, 0], [(-1/f), 1]])

from sympy.abc import theta
from sympy import sin
def Sylvester(A, B, C, D, N):
    return (1/sin(theta))*Matrix([[A*sin(N*theta)-sin(N-1)*theta, B*sin(N*theta)], [C*sin(N*theta), D*sin(N*theta)-sin(N-1)*theta]])