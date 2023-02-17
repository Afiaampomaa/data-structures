import numpy as np
L = 12   #given span
w = 10    #given udl intensity
x = [0,12]   #beginning and end of beam
#M=(w*(-6*x**2+6*L*x-L**2))/12   Bending moment expression
#V=w*((L/2)-x)   Shear force expression

#Question 1a
MomentAtEnds=[]
ShearAtEnds=[]
for i in x:
    M=(w*(-6*i**2+6*L*i-L**2))/12
    MomentAtEnds.append(M)
    V=w*((L/2)-i)
    ShearAtEnds.append(V)
print(f"The bending moments at the ends are {MomentAtEnds}kNm")
print(f"The shear forces at the ends are {ShearAtEnds}kN")

#Question 1b
'm0=x**2-12*x+24'
PointOfContraflexure1=6-np.sqrt(12)
PointOfContraflexure2=6+np.sqrt(12)
print(f'The first point of contraflexure is {PointOfContraflexure1}m')
print(f'The second point of contraflexure is {PointOfContraflexure2}m')

#Question 1c
'v0=L/2-x'
DistanceOfZeroShearForce=L/2
print(f'The distance of zero shear force is {DistanceOfZeroShearForce}m')

#Question 1d and 1e 
Bending_at_point=[]
Shearforce_at_point=[]
z=np.arange(0,12.01,0.01)
for j in z:
    BM=(w*(-6*j**2+6*L*j-L**2))/12
    SF=w*((L/2)-j)
    Bending_at_point.append(BM)
    Shearforce_at_point.append(SF)
print(f'The bending moment at points at steps 10mm is {Bending_at_point}kNm')
print(f'The shear force at points at steps 10mm is {Shearforce_at_point}kN')

#Question 1f
BM=(w*(-6*z**2+6*L*z-L**2))/12
SF=w*((L/2)-z)
Abs=abs(BM)
MinimumBM=min(Abs)
Min1=6-np.sqrt(12-(1/30*MinimumBM))
Min2=6+np.sqrt(12-(1/30*MinimumBM))
print(f'First point along the span, L where bending moment is minimum is {Min1}')
print(f'Second point along the span, L where bending moment is minimum is {Min2}')

#Question 1g
#Relative Error=((Min-point of Contraflexure)/Min)*100%
RelativeError1=((PointOfContraflexure1-Min1)/PointOfContraflexure1)*100
RelativeError2=((Min2-PointOfContraflexure2)/PointOfContraflexure2)*100
print(f'Relative Error of First point is {RelativeError1}%')
print(f'Relative Error of Second point is {RelativeError2}%')

#Question 1h
#maximum bending moment occurs at a point where the shear force = 0
#minimum bending moment occurs at the supports

print(f'point where bending moment is maximum is {z[600]}m')
print(f'first point where bending moment is minimum is {z[0]}m')
print(f'second point where bending moment is minimum is {z[1200]}m')




github link:https://github.com/afiaampomaa
