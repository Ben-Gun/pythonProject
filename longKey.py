#принимает непозиционные элементы и выводит элемент с самым длинным ключом
def longKey(**kwargs):
    temp = 0
    lKey = ''
    for i in kwargs.items():
        l = len(i[0])
        if l > temp:
            temp = l
            lKey = i
    return (lKey)

if __name__ == '__main__':
    print(longKey(a=3, bb=2, c=4))
