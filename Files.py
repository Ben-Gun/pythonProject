if __name__ == '__main__':
    num = 0
    res = []
    li = []
    temp = 0
    for i in open('text.txt', 'r+'):
        li = i.split(' ')
        num = int(li[0])
        temp = int(li[-1])
        for j in range(2, len(li)-2, 2):
            if li[j-1] == '*':
                num *= int(li[j])
            if li[j-1] == '/':
                num //= int(li[j])
            if li[j-1] == '-':
                num -= int(li[j])
            if li[j-1] == '+':
                num += int(li[j])
        if temp == num:
            res.append('True')
        else:
            res.append('False')
        f = open('output.txt', 'w+')
        f.write(str(res))
        f.close()
        print(num)
        num = 0
