def sort(array, leftIndex, rightIndex):
    min = leftIndex
    
    for i in range(leftIndex, rightIndex):
        min = i
        for j in range(i+1,rightIndex+1):
            if array[j] < array[min]:
                min = j
        array[i], array[min] = array[min], array[i]

array = [5,800,100,9,8,1,4,0,10,2,-5,-1,80,-80,-800]
print array
sort(array, 0, 14)
print array