if __name__ == '__main__':
    a = {'Война и мир': 'Толстой', 'Анна Коренина': 'Толстой', 'Детсво': 'Толстой', 'Кавказский пленник': 'Толстой',
         'Два товарища': 'Толстой', 'Преступление и наказание': 'Достоевский', 'Братья Карамазовы': 'Достоевский',
         'Бесы': 'Достоевский', 'Белые ночи': 'Достоевский', 'Идиот': 'Достоевский', 'Игрок': 'Достоевский',
         'Мертвые души': 'Гоголь', 'Тарас Бульба': 'Гоголь', 'Ночь перед Рождеством': 'Гоголь', 'Вий': 'Гоголь',
         'Нос': 'Гоголь', 'Портрет': 'Гоголь', 'Миргород': 'Гоголь', 'Каштанка': 'Чехов', 'Ванька': 'Чехов'}
    res = 0
    avtor = {}
    temp = 0
    amount = 0
    for key, value in a.items():
        if value not in avtor:
            avtor.update({value:0})
        if value in avtor:
            avtor[value] +=1
    for i in avtor.items():
        temp = i[1]
        if temp > amount:
            amount = temp
            res = i
    print(res)