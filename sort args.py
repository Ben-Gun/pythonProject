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
    return sorteed
if __name__ == '__main__':
    print(sortA(5, 1, 3, 'z', 'g', 'a'))