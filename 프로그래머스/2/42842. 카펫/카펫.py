def solution(brown, yellow):
    for i in range(1, int(yellow**(1/2)) + 1):  
        if yellow % i == 0:                 
            x = yellow/i                    
            y = i                           
            if brown == (x*2 + y*2 + 4): 
                return [x+2, y+2]