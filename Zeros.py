

def shiftZeros(aList):
    
    if len(aList)==0: 
        return aList  
    
    zeros = 0
    end = len(aList) 
    i = 0
    pivot = 0
    
    while(i<end):
        
        if(aList[i]==0):
            pivot = i if i<pivot else pivot 
            zeros += 1

        if(aList[i]!=0):
            aList[pivot] = aList[i]
            pivot += 1

        i +=1
    
    for z in range(end-zeros, end):
        aList[z] = 0 

    return aList


if __name__ == '__main__':

    
    print "Enter numbers consequently by pressing the number and then 'Enter'"
    print "To move the zeros at the end of the list press any other key\n"
    bList = []
    cond = True
    while cond:
        try:
            x = float(raw_input())
            bList.append(x)    
        except ValueError:
            cond = False
            #print 'Invalid Number'
    
    aList = shiftZeros(bList)
    print aList 
    
    
    