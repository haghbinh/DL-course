import numpy as np
def readarr(n):
    A=np.zeros(n)
    i=0
    while i<n:
        A[i] = eval(input(f"A[{i}]:"))
        i+=1
    return A 

A = readarr(10)      
x = eval(input("Enter x:"))
s=0
i=0
while i<10:
    if A[i]==x:
        s+=1
    i+=1
print("S=",s)
