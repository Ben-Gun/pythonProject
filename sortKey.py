#сортировка непозиционных по ключу
def sortKey(**kwargs):
    sortDict = dict(sorted(kwargs.items()))
    print(sortDict)

if __name__ == '__main__':
    sortKey(v=3, bb=2, c=4)