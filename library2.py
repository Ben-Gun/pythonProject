if __name__ == '__main__':
    #  найти самого пишущего писателя(больше всего книг)

    libriary = ({'Bloody moon': 'M.Stivenson', 'Python programming': 'M. Dauson',
                 'The Python Workbook': 'B. Stepherson', 'Capains dother': 'A. Pushkhin',
                 'Learn Python': 'E. Matith', 'E. Onegin': 'A. Pushkhin'})
    values = list(libriary.values())
    values.sort()
    count = 1
    maxCount = 0
    maxAuthor = ''
    for i in range(len(values)-1):
        if values[i] == values[i+1]:
            count += 1
        else:
            if count > maxCount:
                maxCount = count
                maxAuthor = values[i]
            count = 1

    print(maxCount)
    print(maxAuthor)