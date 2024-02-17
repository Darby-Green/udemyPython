def sumToMagic(x,y):
    for i in range(len(x)):
        for j in range(len(x)):
            if i != j and x[i]+x[j] == y:
                print([i,j])


sumToMagic([8,16,22,35],30)