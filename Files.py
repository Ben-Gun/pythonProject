import os

if __name__ == '__main__':
    li1 = []
    num = 0
    for i in open('text.txt', 'r'):
        li = i.split(' ')
        num = int(li[0])
        for j in range(2, len(li)-2, 2):
            if li[j-1] == '-':
                num -= int(li[j])
            if li[j-1] == '+':
                num += int(li[j])
        print(num)
        num = 0