import sys

f=open(sys.argv[1])
n=int(f.readline())
l1=f.readline().split()
l2=f.readline().split()

a=[0,0,0]
b=[0,0,0]

for i in range (n):
    a[i%3]+=int(l1[i])
    b[i%3]+=int(l2[i])

aireblanche=a[0]*b[0]+a[1]*b[2]+a[2]*b[1]
airejaune=a[1]*b[0]+a[2]*b[2]+a[0]*b[1]
airerose=a[2]*b[0]+a[0]*b[2]+a[1]*b[1]

print(str(airejaune)+" "+str(airerose)+" "+str(aireblanche))