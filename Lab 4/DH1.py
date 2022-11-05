g = 209
p = 991
fc = 1

for x in range(1, p):    
    if (g * x) % p == fc:         
        print(x)        
        break