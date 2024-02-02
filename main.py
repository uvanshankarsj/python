mat=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
res=[]
print(mat[0:][-1])

while mat:
    res+=mat[0][0:]
    mat.pop(0)
    res+=[row[-1] for row in mat]
    
    for i in range(len(mat)):
        mat[i].pop()
    
    res+=mat[i][::-1]
    print(mat)
    mat.pop()
    print(mat)
    tmp=[row[0] for row in mat]
    print(type(tmp))
    res+=reversed(tmp)
    for i in range(len(mat)):
        mat[i].pop(0)
    
    print(res)
