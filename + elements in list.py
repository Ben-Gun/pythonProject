if __name__ == '__main__':
    a = []
    s = int(input('Введите длинну списка:'))

    for i in range(s):
        number = int(input())
        a.append(number)
    for i in range(s):
        if a[i] > 0:
            print(a[i])
