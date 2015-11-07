def sort(array, leftIndex, rightIndex):
    k=0
    
    for i in range(leftIndex, rightIndex):
        print "i = " + str(i)
        for j in range(leftIndex, rightIndex -(k)):
            print "j = " + str(j)
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
        k+=1


array = [800,5,100,9,8,1,4,0,10,2,-5,-1,80,-80,-800]
print array
sort(array, 12, 14)
print array