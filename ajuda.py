def forcaBruta(t,p):
    n=len(t)
    m=len(p)
    i=0
    pcont=0
    cont=0

    while i<=n-m:
        j=0
        while j<m and p[j]==t[i+j]:
            j=j+1
            pcont=pcont+1
            if j>=m:
                
                cont=cont+1

        i=i+1
    print(pcont)

    return cont

def calculaD(p,m):

    i=0
    d=[]
    for i in range(m):
        d.append(0)

    j=0
    k=1
    
    
    while k<m:
        if p[k]==p[j]:
            d[k]=j+1
            k=k+1
            j=j+1
        elif j==0:
           
            d[k]==0
            k=k+1
        else:
            
            j=d[j-1]
            k=k+1

    
    return d



def kmp(t,p):
    d=[]
    d=calculaD(p,len(p))
    n=len(t)
    m=len(p)
    i=0
    j=0
    cont=0


    while i<n:
        if t[i]==p[j]:
            
            i=i+1
            j=j+1

        if j==m:
            cont=cont+1
            j=d[j-1]

        elif i<n and p[j]!=t[i]:
            
            if j!=0:
                j=d[j-1]
            else:
                i=i+1

    return cont



t=input("string1")
p=input("string2")



fim=forcaBruta(t,p)
#fim2=kmp(t,p)


print("bruta",fim)





