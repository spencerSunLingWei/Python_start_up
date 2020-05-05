def Kseq(start, stop, step):
    """ (int,int,int) -> list of integers

    Input: This function is passed start (>= 0), stop (>start), and step (>= 1) values that define a sequence of numbers.
    Output: This function returns a list of the corresponding K sequence.

    >>>Kseq(0,6,1)
    [2, 1, 9, 100, 11881, 143544361]
    >>>Kseq(2,6,2)
    [9, 11881]
    """
    
    
    result=[]
    for i in range (start, stop,step):
        x = i
        def K_function (x):
            if x == 0:
                y = 2
            elif x == 1:
                y = 1
            elif x >1:
                y = (K_function(x-1)+K_function(x-2))**2
            return y
        result.append(K_function(x))
        
    return result
    
            
            
            




     
