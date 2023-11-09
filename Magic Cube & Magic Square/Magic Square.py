def MagSquare(n):  
    #creo la matriz
    matriz = [[0 for x in range(n)] 
                      for y in range(n)] 

    i = n / 2
    j = n - 1
    num = 1
    #valores iniciales de i, j y num 
    while num <= (n * n): 
        if i == -1 and j == n: # verificar q no este out of bounds 
            j = n - 2
            i = 0
        else:   
            if j == n: 
                j = 0    
            if i < 0: 
                i = n - 1
        if matriz[int(i)][int(j)]: # poner int hace q se redondee 
            j = j - 2
            i = i + 1
            continue
        else: 
            matriz[int(i)][int(j)] = num 
            num = num + 1
        #valores para siguiente numero
        j = j + 1
        i = i - 1 

    print ("Constante de suma es ",n*(n**2+1)/2) 
    for i in range(0, n): 
        for j in range(0, n): 
            print('%3d ' % (matriz[i][j]),end = '') 
            if j == n - 1:  
                print() #endl


print("Magic square!!!")
while True:
    inp = input("Da valor de n, para hacer el cuadro mágico n x n : ")
    try:
        n = int(inp)
    except ValueError:
        print("da numero impar igual o mayor a 3.")
        continue
    if n >= 3 and n % 2 == 1:
        break
    else:
        print("da numero impar igual o mayor a 3.")

MagSquare(n)

