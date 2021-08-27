def compareTriplets(a,b):
    ans = []
    x=0
    y=0
    for i in range(0,len(a)):
        if(a[i]>b[i]):
            x=x+1
        elif(a[i]<b[i]):
            y=y+1
        else:
            continue
    ans.append(x)
    ans.append(y)
    return ans