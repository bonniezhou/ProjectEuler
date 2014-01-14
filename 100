#100

import math

y = 10**12
while True:
    denom = y*(y-1)
    if denom%2 == 0:
        x = math.sqrt(denom/2)
        numer = int(x)*(int(x)+1)
        if float(numer)/denom == 0.5:
            print int(x)+1, y
            break
        else:
            y = y+1
    else:
        y = y+1
