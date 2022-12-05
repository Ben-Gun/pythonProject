if __name__ == '__main__':
    temp = total = 0
    a = int(input())
    while a != 0:
        if a == temp:
            total = total + 1
        temp = a
        a = int(input())
        if total == 0:
            total = 1
    print(total)