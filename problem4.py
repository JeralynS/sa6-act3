
def intersection(list1, list2):
    intersected = list(filter(lambda x: x in list2, list1))
    return intersected

list1 = [5, 6, 7, 8, 9]
list2 = [2, 3, 4, 5, 6]

new_list = intersection(list1, list2)
print(f'Intersection:\n{new_list}')