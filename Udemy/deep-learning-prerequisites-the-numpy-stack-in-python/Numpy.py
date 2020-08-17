import numpy as np 
l=[1,2,3]
a=np.array([1,2,3])
for b in a:
    print b
l.append(4)
print l
#a.append(4)
l += [5]
print l
a = a + np.array([4])
print a
print 2*a
print 2*l
print l + l
l2=[]
for e in l:
    l2.append(e+3)
print l2
l2=[e+3 for e in l]
print l2
l2=[]
for e in l:
    l2.append(e**3)
print l2
print a**2
print np.sqrt(a**2)

# Dot Product

a=np.array([1,2])
b=np.array([3,4])
dot =0
for e,f in zip(a,b):
    dot +=e*f
print dot
dot =0
for i in range(len(a)):
    dot += a[i] * b[i]
print dot
print a*b
print np.sum(a*b)
print (a *b).sum
print np.dot(a,b)
print a.dot(b)
amag=np.sqrt((a * a).sum())
print amag
bmag=np.sqrt((b*b).sum())
print bmag
print np.linalg.norm(a)
print np.linalg.norm(b)
cosangle = a.dot(b)/(np.linalg.norm(a) * np.linalg.norm(b))
print cosangle
l=[[1,2],[3,4]]
print l
print l[0]
Am=np.array(l)
print Am
print Am[:,0]
print Am.T
print np.exp(Am)
print np.exp(l)
b=np.array([[1,2,3],[4,5,6]])
print Am.dot(b)
print np.linalg.det(Am)
print np.linalg.inv(Am)
# Always avoid inverse
print np.trace(Am)
print np.diag(Am)
print np.diag([1,4])

# Eigen values and vectors

print np.linalg.eig(Am)

Lam,V=np.linalg.eig(Am)
print Lam
print  V
print V[:,0] * Lam[0] , Am.dot(V[:,0])
print V[:,0] * Lam[0] == Am.dot(V[:,0])
print np.allclose(V[:,0] * Lam[0] , Am.dot(V[:,0]))
print np.linalg.eigh(Am)

# problem linear equations
# x1 + x2 =2200 2 eq and 2 unknows
# 1.5x1 + 4x2 = 5050
a=np.array([[1,1],[1.5,4]])
b=np.array([2200,5050])
x = np.linalg.solve(a,b)
print x
print np.linalg.inv(a).dot(b)