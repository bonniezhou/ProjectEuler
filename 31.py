#31

def collapse(nested_list):
    new_list = []
    for list in nested_list:
        new_list = new_list + list
    return new_list

def how_many(n, list):
    count = 0
    for i in list:
        if i == n:
            count = count + 1
    return count

def distribute(num, list):
    for i in range(0, len(list)):
        list[i] = list[i] + num
    return list

def loop(c1, c2, c3):
    c2_new = []
    c3_new = []
    for i in range(0, len(c2)):
        for j in range(0, len(c1)):
            if c3[i] == c1[j]:
                c2_new.append(distribute(c2[i], c1[j:]))
                c3_new.append(c1[j:])
    c2 = collapse(c2_new)
    c3 = collapse(c3_new)
    return [c2,c3]

def combos(coins, k):
    count = 1
    coins1 = [] + coins
    coins2 = [] + coins
    while count < k:
        list = loop(coins, coins1, coins2)
        coins1 = list[0]
        coins2 = list[1]
        count = count + 1
    return coins1

def list_count(list, n):
    count = 0
    for i in list:
        if i == n:
            count = count + 1
    return count

list1 = combos([0,1,2,5,10,20],50)
n1 = 50

#print list1
print list_count(list1, n1)
