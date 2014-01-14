#9 Special Pythagorean triplet
import math
a = 1
while a <= 332:
    for b in range(a,(1000-a)/2):
        c = math.sqrt(a**2 + b**2)
        if c % int(c) == 0.0:
            if a + b + int(c) == 1000:
                print a, b, c
    a = a + 1
