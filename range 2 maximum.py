if __name__ == '__main__':
    preNumber = int(input())
    number = int(input())
    postNumber = int(input())

    count = 0
    count2 = 0
    total = 0

    while postNumber != 0:
        if number > postNumber and number > preNumber:
           while number >= postNumber != 0:
               count += 1
               preNumber = number
               number = postNumber
               postNumber = int(input())
               if total <= count:
                  total = count
        count = 0
        preNumber = number
        number = postNumber
        if postNumber == 0:
            break
        postNumber = int(input())

    print(total)
