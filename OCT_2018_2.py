n=int(input())
l2=[]
for i in range(n):
    l2.append(int(input()))

    
for k in range(n):
    
    l1=[0]*3
    
    if(int(l2[k]%26)<=2 and l2[k]%26>0):
        if(int(l2[k]/26)==0):
            l1[0]=1
        else:
            l1[0]=2**(int(l2[k]/26))
    #elif()
        
    elif(int(l2[k]%26)>2 and int(l2[k]%26)<=10):
        if(int(l2[k]/26)==0):
            l1[1]=1
        else:
            l1[1]=2**int(l2[k]/26)
    
    else:
        if(int(l2[k]%26)==0):
            l1[2]=2**int((l2[k]/26)-1)
        else:
            l1[2]=2**(int(l2[k]/26))
    
    
    for f in range(3):
        print(l1[f],sep='\n',end=' ')
        
    print('\n')    