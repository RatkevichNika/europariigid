import random
slovar = {'Estonia': 'Tallinn',  'Tallinn' : 'Estonia',  'Riga': 'Latvia', 'Latvia': 'Riga', 'Finland': 'Helsinki', 'Helsinki': 'Finland', 'Sweden': 'Stockholm', 'Stockholm': 'Sweden', 'Italy': 'Rome', 'Rome': 'Italy', 'Portugal': 'Lissabon', 'Lissabon': 'Portugal'}
def add_to_slovar():
    riik = input('Добавьте страну: ')
    linn = input('Добавьте столицу: ')
    slovar[riik] = linn
    slovar[linn] = riik
def change(town):
    del slovar[town]
    new_slovar_value=input('Поменяйте город: ')
    slovar[town] = new_slovar_value
    slovar[new_slovar_value] = town
def test():
    count = 0
    listik=[]
    for element in slovar.keys():
        listik.append(element)
    for i in range(10):
        random_element = random.sample(listik, 1)[0]
        print(random_element)
        test_write = input('Напишите: ')
        i += 1
        if test_write == slovar[random_element]:
            print('Правильно!')
            count=count+1
        else:
            print('Неправильно')
    print('Вы написали тест на ',count*10,'%.')

while True:
    print("Напишите 1, если хотите написать страну или город")
    print("Напишите 2 если хотите проверить свои знания")
    choose=input()
    if choose=='1':
        town = input('напишите город или страну: ')
        if town in slovar.keys():
            output = slovar[town]
            print(output)  
            print('Если это неправильно, вы хотите изменить это?\nДа или Нет?')
            a=input()
            while True:
                if a=='Да':
                    change(town)
                    break
                elif a == 'Нет':
                    break
                else:
                    print('Неправильно!')
                    a=input('попробуйте занаво: ')
        else:
            print('Не существует')
            print('Введите «1», если вы хотите добавить ')
            print('Введите «2», если вы не хотите добавить ')
            valik=input()
            while True:
                if valik=='1':
                    add_to_slovar()
                    break
                elif valik=='2':
                    break
                else:
                    print('Неправильно!')
                    valik=input('Поробуйте занаво: ')
                    break
    elif choose=='2':
        test()
    else:
        print('Неправильно!')
        choose=input('Попробуйте занаво: ')
