#17 Number letter counts
units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def list_len(list):
    l = 0
    for i in list:
        l = l + len(i)
    return l

def prod_len(list1, list2):
    l = 0
    for i in list1:
        for j in list2:
            l = l + len(i)+len(j)
    return l

length_99 = list_len(units) + list_len(teens) + list_len(tens) + prod_len(tens, units)
length_hun = prod_len(units, ["hundred"])*100 + len("and")*99*9 + length_99*9 
length_total = length_99 + length_hun + len("onethousand")

print length_total
