def sort(array, leftIndex, rightIndex):
    k = 0
    for i in range(leftIndex, rightIndex):

        for j in range(leftIndex+k, rightIndex -i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        for j in range(rightIndex+leftIndex-i-1, i-1, -1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        
        k=k+1



array = [5,800,100,9,8,1,4,0,10,2,-5,-1,80,-80,-800]
print array
sort(array, 13, 14)
print array