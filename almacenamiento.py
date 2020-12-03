def maximizar(As, D):
    optimoGlobal = []
    while D>0:
        optimoLocal = archivoMinimo(As)
        if(D-optimoLocal[1]<0):
            break
        else:
            D=D-optimoLocal[1]
            optimoGlobal.append(optimoLocal)
    return optimoGlobal

def archivoMinimo(As):
    min1 = As[0] 
    for i in range(len(As)): 
        if As[i][1] < min1[1]:  
            min1 = As[i]
    As.remove(min1)
    return min1
