if __name__ == '__main__':
    m = int(input())
    n = int(input())
    a = 1

    for i in range(m, n+1):
        while a*2 <= i:
            if i % a == 0:
                if a == 1 or a == i:
                    a += 1
                    continue
                else:
                    print(i, a)
            a += 1
        a = 1
