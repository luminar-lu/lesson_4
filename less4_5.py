from functools import reduce
nums = (el for el in range(100, 1001, 2))
list_1 = list(nums)
result = reduce(lambda x,y: x * y, list_1)
print(result)