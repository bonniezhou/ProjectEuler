#12 Highly divisible triangular number
import math
triangle = 1
natural = 2
num_div = 0
total_divs = 0
#------------------------------
while num_div <= 50:
    triangle = triangle + natural
    natural = natural + 1
    num_div = 0
    for div in range (1, triangle + 1):
        if triangle % div == 0:
            num_div = num_div + 1
print triangle
#Too inefficient.

#------------------------------
while total_divs <= 500:
    triangle = triangle + natural
    natural = natural + 1
    num_div = 0
    for div in range (1, int(math.sqrt(triangle)) + 1):
        if triangle % div == 0:
            num_div = num_div + 1
    total_divs = num_div*2
print triangle
#No triangle number is also a square except for 1.
