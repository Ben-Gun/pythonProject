if __name__ == '__main__':
    a = []
    s = int(input('Введите длинну списка:'))

    for i in range(s):
        number = int(input())
        a.append(number)
    for i in range(s):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            print(a[i])
#элементы больше предыдущего