n=int(input())
l2=[]


for _ in range(n):
    l=list(map(int,input().split()))
    
    if(int((l[0]+l[1])/l[2])%2==0):
        
        l2.append("CHEF")
    else:
        l2.append("COOK ")
        
for i in range(len(l2)):
    print(l2[i],sep='\n')
