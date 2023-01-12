if __name__ == '__main__':
    num = 0
    res = []
    li = []
    temp = 0
    decision = 0
    for i in open('text.txt', 'r+'):
        li = i.split(' ')
        decision = int(li[-1])
        for j in range(1, len(li)-2, 2):
            if li[j] == '*':
                temp = int(li[j-1]) * int(li[j+1])
                continue
            elif li[j] == '/':
                temp = int(li[j-1]) // int(li[j+1])
                continue
            if li[j] == '*':
                temp = temp * int(li[j + 1])
            elif li[j] == '/':
                temp = temp // int(li[j + 1])
        for j in range(2, len(li)-2, 2):
            if li[j-1] == '*':
                continue
            if li[j-1] == '/':
                continue
            if li[j-1] == '-':
                num -= int(li[j])
            if li[j-1] == '+':
                num = int(li[j])
        num = num + temp
        if decision == num:
            res.append('True')
        else:
            res.append('False')
        f = open('output.txt', 'w+')
        f.write(str(res))
        f.close()
        print(num)
        num = 0
