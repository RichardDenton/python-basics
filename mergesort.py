def mergesort(aList):
    """
    Takes in a list of unsorted items and sorts the list in ascending order.
    """
    #If list length is less than 2 the list is already sorted
    if len(aList) < 2:
        return aList
    
    #Split the list in half
    centre = len(aList) // 2
    leftHalf = aList[:centre]
    rightHalf = aList[centre:]
    
    #Keep splitting each half until the list length is less than 2
    mergesort(leftHalf)
    mergesort(rightHalf)
    
    #Merge the lists
    a = 0
    b = 0
    c = 0
    
    while a < len(leftHalf) and b < len(rightHalf):
        if leftHalf[a] < rightHalf[b]:
            aList[c] = leftHalf[a]
            a += 1
            c +=1
        else:
            aList[c] = rightHalf[b]
            b += 1
            c += 1
            
    while a < len(leftHalf):
        aList[c] = leftHalf[a]
        a += 1
        c += 1
        
    while b < len(rightHalf):
        aList[c] = rightHalf[b]
        b += 1
        c += 1
   
