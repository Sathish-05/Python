pos=[]
n=list(map(int,input().split(",")))
for i in range(len(n)):
    if n[i]>=0:
        pos.append(n[i])
    else:
        continue
print(pos)_