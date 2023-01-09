if __name__ == '__main__':
    a = {'Pencil': [10, 15], 'Pen': [12, 40], 'Eraser': [5, 30], 'Backpack': [1, 400], 'Notebook': [5, 50]}
    temp = 0
    amount = 0
    res = []
    for i in a.items():
        temp = i[1]
        if temp[0] > amount:
            amount = temp[0]
            res = i
    print(res[0], amount)
