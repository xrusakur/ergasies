import math



def calculateSD(aList):
    
    if(len(aList)==0): 
        return 0
    
    sumList = 0
    for i in aList: 
        sumList += i 
    avg = sumList/len(aList)
    
    sumSquared = 0
    for i in aList: 
        sumSquared += (i-avg)*(i-avg)
        
    return math.sqrt(sumSquared/len(aList))     
    
        

if __name__ == '__main__':

    
    print "Enter numbers consequently by pressing the number and then 'Enter'"
    print "To compute the standard deviation press any other key\n"
    bList = []
    cond = True
    while cond:
        try:
            x = float(raw_input())
            bList.append(x)    
        except ValueError:
            cond = False
            #print 'Invalid Number'

    print calculateSD(bList)
    
    