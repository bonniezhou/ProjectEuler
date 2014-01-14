#24 Lexicographic permutations

#is_descending: list(int) -> list(int)
def is_descending(list):
    index = 0
    while index <len(list)-1:
        if list[index] < list[index+1]:
            return False
        index = index + 1
    else:
        return True

#selection sort. pass in [] as new_list parameter.
#sort_ascend: list(int) [] -> list(int)
def sort_ascend(list, new_list):
    smallest = list[0]
    index = 0
    while index < len(list)-1:
        if list[index+1] < smallest:
            smallest = list[index+1]
        index=index + 1
    new_list.append(smallest)
    list.remove(smallest)
    if len(list) != 0:
        sort_ascend(list, new_list)
    return new_list

#next_biggest: int list(int, w/o num, desc order) -> int
def next_biggest(num, list):
    next = list[0]
    for n in list:
        if n > num and n < next:
            next = n
    return next

#next_perm: list(int) -> list(int)
def next_perm(list):
    index = -1
    end_list = list[index:]
    #find an end_list not in descending order
    while is_descending(end_list)== True:
        index = index - 1
        end_list = list[index:]
        if index == -len(list)-1:
            return None

    #find index of front+1 and swap with front
    front = end_list[0]
    rest = end_list[1:]
    next = next_biggest(front, rest)
    rest.remove(next)
    rest.append(front)
    return list[:index]+[next]+sort_ascend(rest,[])
    
count = 1
perm = [0,1,2,3,4,5,6,7,8,9]
index = len(perm)
while count < 1000000:
    perm = next_perm(perm)
    count = count + 1
print count, perm
