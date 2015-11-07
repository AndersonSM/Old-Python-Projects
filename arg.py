def sort(A, m, k):
    a = A[m:k+1]
    
    C = []
    maior = 0
    for i in a:
        if i > maior:
            maior = i

    for i in range(maior+1):
        C.append(0)

    for j in range(0,len(a)):
        C[(a[j]-1)] += 1
    
    #sum = 0
    #for i in range(1, len(C)):
    #    dum = C[i]
    #    C[i] = sum
    #    sum += dum
    
    for i in range(1, len(C)):
        C[i] = C[i] + C[i-1]
    
    B = []
    for j in range(len(a)):
        B.append(a[j])
    
    for i in range(len(a)):
        print C[a[i]]
        B[C[a[i]]] = a[i]
        C[a[i]] += 1
    
    D = []
    for i in range(len(A)):
        if i >= m and i <= k:
            D.append(B[i-m])
        else:
            D.append(A[i])
    
    print D

A = [2,4,8,1,5,7,3]

sort(A, 0, 6)