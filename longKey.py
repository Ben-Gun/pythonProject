#принимает непозиционные элементы и выводит элемент с самым длинным ключом
def longKey(**kwargs):
    temp = 0
    lKey = dict
    for i in kwargs.items():
        l = len(i[0])
        if l > temp:
            temp = l
            lKey = i
    print(lKey)

if __name__ == '__main__':
    longKey(a=3, bb=2, c=4)
