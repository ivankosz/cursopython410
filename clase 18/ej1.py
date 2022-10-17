def multi_total (num):
    res = 1
    for i in range (num):
        res *= (i+1)
    return res

print(multi_total (6))

