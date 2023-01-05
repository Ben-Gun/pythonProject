#сортировка непозиционных по ключу
def sortKey(**kwargs):
    sortDict = dict(sorted(kwargs.items()))
    return sortDict

if __name__ == '__main__':
    print(sortKey(v=3, bb=2, c=4))