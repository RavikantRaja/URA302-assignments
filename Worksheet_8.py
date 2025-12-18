
import math

print("Q1")
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

A=Point(2,3)
B=Point(6,7)
d=math.sqrt((B.x-A.x)**2+(B.y-A.y)**2)
print(d)

mx=(A.x+B.x)/2
my=(A.y+B.y)/2
print(mx,my)

m=(B.y-A.y)/(B.x-A.x)
c=A.y-m*A.x
print("y=",m,"x+",c)

C=Point(4,2)
x0,y0=C.x,C.y
a=m
b=-1
c1=c
d1=(a*x0+b*y0+c1)/(a*a+b*b)
xr=x0-2*a*d1
yr=y0-2*b*d1
print(xr,yr)

print("Q2")
A=[2,1]
B=[-1,3]
C=[4,2]

R=[A[0]+B[0]+C[0],A[1]+B[1]+C[1]]
print(R)

def mag(v):
    return math.sqrt(v[0]**2+v[1]**2)

print(mag(A),mag(B),mag(C))

def dot(u,v):
    return u[0]*v[0]+u[1]*v[1]

print(dot(A,B),dot(A,C),dot(B,C))

def angle(u,v):
    return math.degrees(math.acos(dot(u,v)/(mag(u)*mag(v))))

print(angle(A,B),angle(A,C),angle(B,C))

proj=[(dot(A,B)/dot(B,B))*B[0],(dot(A,B)/dot(B,B))*B[1]]
print(proj)

print("Q3")
S=[1,2]
E=[6,5]
P=[4,1]

L=mag([E[0]-S[0],E[1]-S[1]])
print(L)

t=((P[0]-S[0])*(E[0]-S[0])+(P[1]-S[1])*(E[1]-S[1]))/((E[0]-S[0])**2+(E[1]-S[1])**2)
t=max(0,min(1,t))
Cpt=[S[0]+t*(E[0]-S[0]),S[1]+t*(E[1]-S[1])]
print(Cpt)

dist=mag([P[0]-Cpt[0],P[1]-Cpt[1]])
print(dist)

print("Q4")
a1,b1,c1=2,3,6
a2,b2,c2=4,6,12

D=a1*b2-a2*b1
if D!=0:
    x=(c1*b2-c2*b1)/D
    y=(a1*c2-a2*c1)/D
    print(x,y)
else:
    print("Lines are parallel or coincident")
