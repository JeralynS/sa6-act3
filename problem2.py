
strings = ["fourty", "six", "no", "rainbow", "real"]

sort_order = sorted(strings, key=lambda x: (len(x), x))
print(f'Sorted list:\n{sort_order}')