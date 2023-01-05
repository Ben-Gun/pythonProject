#принимает непозиционные элементы и выводит элемент с самым длинным ключом
def longKey(**kwargs):
    temp = 0
    lKey = ''
    for i in kwargs.items():
        j = len(i[0])
        if j > temp:
            temp = j
            lKey = i
    print(lKey)

if __name__ == '__main__':
    longKey(a=3, bb=7, ckk=4)
