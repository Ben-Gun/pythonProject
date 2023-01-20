def is_prime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return x

a = [1, 20, 35, 17, 20, 61, 21, 8]
res = []
for i in a:
    if is_prime(i) == False:
        continue
    else:
        res.append(is_prime(i))
print(res)