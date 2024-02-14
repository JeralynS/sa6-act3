
def find_max(numbers, compare_fun):
    maximum = numbers[0]
    for num in numbers[1:]:
        if compare_fun(num, maximum) > maximum:
            maximum = num
    return maximum

numbers = [2, 9, 15, 1, 12, 5]
greater_num = lambda x,y: x if x > y else y
max_num = find_max(numbers, greater_num)
print(max_num)
