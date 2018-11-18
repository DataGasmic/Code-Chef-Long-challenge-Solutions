# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 20:59:38 2018

@author: PRANJAL
"""

n=int(input())
h=n
l2=[]
for z in range(n):
    
    l=list(map(int,input().split()))
    
    a=l[0]
    b=l[1]
    c=l[2]
    d=l[3]
    e=l[4]
    
    
    
    for x in range(1,a+1):
        y=a-x
        
        if((x+b==d and y+c==e) or (x+b==e and y+c==d) or (x+c==d and y+b==e) or (x+c==e and y+b==d)):
            m=1
        else:
            m=0
        
            
                
    for x in range(1,b+1):
        y=b-x
        
        if((x+a==d and y+c==e) or (x+a==e and y+c==d) or (x+c==d and y+a==e) or (x+c==e and y+a==d)):
            n=1
        else:
            n=0
            
        
    
    for x in range(1,c+1):
        y=a-x
        
            
       
        if((x+b==d and y+a==e) or (x+b==e and y+a==d) or (x+a==e and y+b==d) or (x+a==d and y+b==e)):
            o=1
        else:
            o=0
                
    if(m==1 or n==1 or o==1):
        l2.append("YES")
        
    else:
        l2.append("NO")


for k in range(h):
    print(l2[k],sep='\n')
    


    
            