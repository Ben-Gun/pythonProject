if __name__ == '__main__':
    a = [4, 2, 6, 9, 0, 1]

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
        print(a)
