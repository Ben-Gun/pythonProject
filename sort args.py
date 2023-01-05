#сортировка позиционных элементов
def sortA(*args):
    sorteed = []
    for i in args:
        if isinstance(i, int):
            i = str(i)
            sorteed.append(i)
        else:
            sorteed.append(i)
    sorteed.sort()
    print(sorteed)

if __name__ == '__main__':
    sortA(5, 1, 3, 'z', 'g', 'a')
