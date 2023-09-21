inpu = "((())"


def fun(inp): 
    count = 0
    
    for i in range(0,len(inp)):
        if inp[i] == "(":
            count += 1
        elif input[i] == ")": 
            count -= 1
            
    return count    

print(fun(inpu))