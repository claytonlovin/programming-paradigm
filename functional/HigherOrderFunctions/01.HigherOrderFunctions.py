############## Higher Order Functions #####################

def map_and_filter(nums, map_func, filter_func):
    return list(filter(filter_func, map(map_func, nums)))

def square(num):
    return num ** 2

def is_odd(num):
    return num % 2 == 1

nums = [1, 2, 3, 4, 5]

result = map_and_filter(nums, square, is_odd)
print(result)  # Saída: [1, 9, 25]

