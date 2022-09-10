import random
def unico(x,L):
  esUnico=True
  for i in range(len(L)):
    if x==L[i]:
      esUnico=False
      break
  return esUnico
L=[]
j=0
while j==x:
    for x in range(2):
     x=random.randrange(0,50,1)
    if unico(x,L):
        L.append(x)
        j+=1
    print(L)
    L.sort()
    print(L)