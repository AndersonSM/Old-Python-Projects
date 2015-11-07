def sort(array, leftIndex, rightIndex):
    for j in range(leftIndex+1, rightIndex+1):
        key = array[j]
        i = j-1
        while i >= leftIndex and array[i] > key:
            array[i+1] = array[i]
            i = i-1
        array[i+1] = key
        
array = [5,800,100,9,8,1,4,0,10,2,-5,-1,80,-80,-800]
print array
sort(array, 0, 2)
print array