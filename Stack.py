
def checkFormula(formula):
    
    stack = []
    push = 0
    pull = 0
    
    for c in formula:
        
        if (c == '{'): 
            stack.append(c)
            push += 1
        
        if (c == '['): 
            stack.append(c)
            push += 1

        if (c == '('): 
            stack.append(c)
            push += 1
            
        if (c == '}'): 
            if(len(stack)<=0): return False;
            a = stack.pop()
            
            if(a != '{'): return False;
            pull += 1
        
        if (c == ']'): 
            if(len(stack)<=0): return False;
            a = stack.pop()
            
            if(a != '['): return False;    
            pull += 1
            
        if (c == ')'): 
            if(len(stack)<=0): return False;
            a = stack.pop()
            
            if(a != '('): return False;    
            pull += 1

                
    if(push!=pull): 
        return False;
         
    return True   



if __name__ == '__main__':
    

    
    #print raw_input("Give the stream of parenthesis to be checked")
    x = raw_input("Give the stream of parenthesis to be checked\n")
    response = checkFormula(x)
    print x + ' is ' + str(response)
