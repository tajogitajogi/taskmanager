q=['10.12.2022','20.10.2000']
z=[19,24]
a=[]
for i in range( len(q)):
    w=q[i].split('.')
    mod=z[i]//8 
    w[0]=str(int(w[0])+mod)
    a.append('.'.join(w))
print(a)