class Person:
    def __init__(self, name, surName, age, telephone, amount):
        self.__name = name
        self.__surName = surName
        self.__age = age
        self.__telephone = telephone
        self.__amount = amount

    def get_name(self):
        return self.__name
    def get_surName(self):
        return self.__surName
    def get_age(self):
        return self.__age
    def get_telephone(self):
        return self.__telephone
    def get_amount(self):
        return self.__amount

    def set_name(self, name):
        self.__name = name
    def set_surName(self, surName):
        self.__surName = surName
    def set_age(self, age):
        self.__age = age
    def set_telephone(self, telephone):
        self.__telephone = telephone
    def set_amount(self, amount):
        self.__amount = amount

    def info(self):
        print(f'name = {self.__name}\n'
              f'surName = {self.__surName}\n'
              f'age = {self.__age}\n'
              f'telephone = {self.__telephone}')

class Manager:
    def __init__(self, name, surName, department):
        self.__name = name
        self.__surName = surName
        self.__department = department
    def get_name(self):
        return self.__name
    def get_surName(self):
        return self.__surName
    def get_department(self):
        return self.__department

    def set_name(self, name):
        self.__name = name
    def set_surName(self, surName):
        self.__surName = surName
    def set_department(self, department):
        self.__name = department

    def info(self):
        print(f'name = {self.__name}\n'
              f'surName = {self.__surName}\n'
              f'department = {self.__department}')

person = Person('Alex', 'Sidorov', 29, '+375297770707', 450)
person1 = Person('Valera', 'Ivanov', 27, '+375291111911', 550)
person2 = Person('Anna', 'Kislaya', 77, '+375295550505', 900)
person3 = Person('Bob', 'Baffet', 66, '+375291110101', 220)
person4 = Person('Chy', 'Ki', 21, '+375293330102', 720)

manager = Manager('Mike', 'Smith', 1)
manager1 = Manager('Jack', 'Wilson', 2)
manager2 = Manager('Tom', 'Lewis', 3)

#сумма всех возрастов всех пользователей
a = []
a.append(person.get_age())
a.append(person1.get_age())
a.append(person2.get_age())
a.append(person3.get_age())
a.append(person4.get_age())
#print(sum(a))

#самый старый человек
list = [person, person1, person2, person3, person4]
oldest_person = person

for i in list:
    if i.get_age() > oldest_person.get_age():
        oldest_person = i
oldest_person.info()

#ищем пользователя по номеру телефона
tel = input()
for i in list:
    if i.get_telephone() == tel:
        i.info()

dict = {person : manager,
       person2 : manager1,
       person1 : manager,
       person3 : manager2,
       person4 : manager2}
res = {}
for key, value in dict.items():
    if value not in res:
        res.update({value: key.get_amount()})
    else:
        res[value] += key.get_amount()
for key, value in res.items():
    key.info()
    print("Manager's income =", f'{value}\n')
