#40 Champernowne's constant

num = 1
length = 0
prev_len = 0
list = [1,10,100,1000,10000,100000,1000000]
digits=[]

while length < 1000000:
    length = length + len(str(num))
    if length >= list[0]:
        d = str(num)[list[0]-prev_len-1]
        digits.append(d)
        list.remove(list[0])
    num = num + 1
    prev_len = length

print digits
