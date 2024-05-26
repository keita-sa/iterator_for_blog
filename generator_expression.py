x = [1, 2, 3, 4, 5]

gen = (i**2 for i in x)

print(gen)
# <generator object <genexpr> at 0x7fa53d8a2890>

print(list(gen))
# [1, 4, 9, 16, 25]