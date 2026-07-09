print('Чонгук ищет в заброшенном замке строчки от его ране написанных песен и хочет выбраться, пока его не нашли злоумышлиники.')
print('Играть нужно за Чонгука. Он потерял текст своей песни и не может выбраться из замка. Противостоят ему хейторы, которые хотят уничтожить к-поп.')
print('У замка один этаж. Это прямоугольник 1 на 2, всего 2 комнаты. Из любой комнаты можно перейти в соседнюю.')
print('Выберете действие,с которого вы хотите начать игру. Действия которые может выполнять Чонгук: перемещение, атака, побег, поиск улик.')
print('Выберете кол-во монстров в комнате, в которую вы отправитесь.')
a = input()
b = int(input())
if a == 'атака':
    if b != 0:
        print('бьюсь с монстрами')
    else:
        print('Атаковать некого. Комната пуста.')
elif a == 'перемещение' or a == 'поиск улик':
    if b != 0:
        a == 'побег'
        if a == 'перемещение' or a == 'поиск улик':
            print('убегаю')
    elif b == 0:
        if a == 'перемещение':
            print('хожу')
        elif a == 'поиск улик':
            print('обыскиваю комнату')
if a == 'атака' and b != 0:
    import random
    hero_hp = random.randint(1, 16)
    hero_punch = random.randint(1, 16)
    monster_hp = random.randint(1, 16)
    monster_punch = random.randint(1, 16)
    while hero_hp > 0 and monster_hp > 0:
        monster_hp = monster_hp - hero_punch
        if monster_hp <= 0:
            monster_hp = 0
            print('Герой наносит удар. Здоровье монстра: 0')
        else:
            print('Герой наносит удар. Здоровье монстра:', monster_hp)
            hero_hp = hero_hp - monster_punch
            if hero_hp < 0:
                hero_hp = 0
            print('Монстр наносит удар. Здоровье героя:', hero_hp)
if a == 'побег' and b != 0:
    print('выберите 1 или 2 комнату')
    import random
    monster = random.random()
    room = int(input())
    if monster > 1:
        print('Монстр атакует. Жизнь закончилась.')
    else:
        if room == 1:
            print('Вы переместились в комнату 2.')
        elif room == 2:
            print('Вы переместились в комнату 1.')
while a == 'поиск улик' and b != 0:
    print('Введите пароль, чтобы найти улику. По скрипту - в пароле 6 букв')
    d = input()
    if d != 'смерть':
        print('Упс... У вас есть ещё 2 попытки. Введите любую букву алфавита, чтобы разгадать пароль')
        r = 'смерть'
        word = r
        new_word = ''
        for i in range(6):
            print('Попытка', i + 1, 'из 6')
            letter = input()
            k = 1
            flag = False
            for sym in word:
                if sym == letter:
                    print('Буква нашлась на месте', k)
                    flag = True
                    new_word += sym
                k += 1
            if flag == False:
                print('Буква не нашлась')
        print('Попробуйте ещё разок:0/. Введите слово>.')
        new_word = input()
        if new_word == word:
            print('Пароль подошёл!')
            break
        else:
            print('Пароль не подошёл')
            print('У вас есть шанс. У вас опять 3 попытки>>.')
    else:
        print('Молодец, ты нашёл пароль!')
        break
print('Вы хотите продолжить игру?')
f = input()
if f =='ДА' or f == 'Да' or f == 'дА' or f =='да' or f == 'конечно' or f == 'Конечно' or f =='КОНЕЧНО':
    print('Выберете действие,с которого вы хотите продолжить игру.')
    print('Действия которые может выполнять Чонгук: перемещение, атака, побег, поиск улик')
    print('Выберете кол-во монстров в комнате, в которую вы отправитесь.')
    a = input()
    b = int(input())
    if a == 'атака':
        if b != 0:
            print('бьюсь с монстрами')
        else:
            print('Атаковать некого. Комната пуста.')
    elif a == 'перемещение' or a == 'поиск улик':
        if b != 0:
            a == 'побег'
            if a == 'перемещение' or a == 'поиск улик':
                print('убегаю')
        elif b == 0:
            if a == 'перемещение':
                print('хожу')
            elif a == 'поиск улик':
                print('обыскиваю комнату')
    if a == 'атака' and b != 0:
        import random
        hero_hp = random.randint(1, 11)
        hero_punch = random.randint(1, 11)
        monster_hp = random.randint(1, 11)
        monster_punch = random.randint(1, 11)
        while hero_hp > 0 and monster_hp > 0:
            monster_hp = monster_hp - hero_punch
            if monster_hp <= 0:
                monster_hp = 0
                print('Герой наносит удар. Здоровье монстра: 0')
            else:
                print('Герой наносит удар. Здоровье монстра:', monster_hp)
                hero_hp = hero_hp - monster_punch
                if hero_hp < 0:
                    hero_hp = 0
                print('Монстр наносит удар. Здоровье героя:', hero_hp)
    if a == 'побег' and b != 0:
        print('выберите 1 или 2 комнату')
        import random
        monster = random.random()
        room = int(input())
        if monster > 1:
            print('Монстр атакует. Жизнь закончилась.')
        else:
            if room == 1:
                print('Вы переместились в комнату номер 2.')
            elif room == 2:
                print('Вы переместились в комнату номер 1.')
    while a == 'поиск улик' and b != 0:
        print('Введите пароль, чтобы найти улику. По скрипту - в пароле 6 букв')
        d = input()
        if d != 'смерть':
            print('Упс... У вас есть ещё 2 попытки. Введите любую букву алфавита, чтобы разгадать пароль')
            r = 'смерть'
            word = r
            new_word = ''
            for i in range(6):
                print('Попытка', i + 1, 'из 6')
                letter = input()
                k = 1
                flag = False
                for sym in word:
                    if sym == letter:
                        print('Буква нашлась на месте', k)
                        flag = True
                        new_word += sym
                    k += 1
                if flag == False:
                    print('Буква не нашлась')
            print('Попробуйте ещё разок:0/. Введите слово>.')
            new_word = input()
            if new_word == word:
                print('Пароль подошёл!')
            else:
                print('Пароль не подошёл')
                print('У вас есть шанс. У вас опять 3 попытки>>.')
        else:
            print('Молодец, ты нашёл пароль!')
            break
else:
    print('Игра закончена<>.')

print('Вы хотите продолжить игру?')
uio = input()
if uio =='ДА' or uio == 'Да' or uio == 'дА' or uio =='да' or uio == 'конечно' or uio == 'Конечно' or uio =='КОНЕЧНО':
    print('Выберете действие,с которого вы хотите продолжить игру.')
    print('Действия которые может выполнять Чонгук: перемещение, атака, побег, поиск улик')
    print('Выберете кол-во монстров в комнате, в которую вы отправитесь.')
    a = input()
    b = int(input())
    if a == 'атака':
        if b != 0:
            print('бьюсь с монстрами')
        else:
            print('Атаковать некого. Комната пуста.')
    elif a == 'перемещение' or a == 'поиск улик':
        if b != 0:
            a == 'побег'
            if a == 'перемещение' or a == 'поиск улик':
                print('убегаю')
        elif b == 0:
            if a == 'перемещение':
                print('хожу')
            elif a == 'поиск улик':
                print('обыскиваю комнату')
    if a == 'атака' and b != 0:
        import random
        hero_hp = random.randint(1, 11)
        hero_punch = random.randint(1, 11)
        monster_hp = random.randint(1, 11)
        monster_punch = random.randint(1, 11)
        while hero_hp > 0 and monster_hp > 0:
            monster_hp = monster_hp - hero_punch
            if monster_hp <= 0:
                monster_hp = 0
                print('Герой наносит удар. Здоровье монстра: 0')
            else:
                print('Герой наносит удар. Здоровье монстра:', monster_hp)
                hero_hp = hero_hp - monster_punch
                if hero_hp < 0:
                    hero_hp = 0
                print('Монстр наносит удар. Здоровье героя:', hero_hp)
    if a == 'побег' and b != 0:
        print('выберите 1 или 2 комнату')
        import random
        monster = random.random()
        room = int(input())
        if monster > 1:
            print('Монстр атакует. Жизнь закончилась.')
        else:
            if room == 1:
                print('Вы переместились в комнату номер 2.')
            elif room == 2:
                print('Вы переместились в комнату номер 1.')
    while a == 'поиск улик' and b != 0:
        print('Введите пароль, чтобы найти улику. По скрипту - в пароле 6 букв')
        d = input()
        if d != 'смерть':
            print('Упс... У вас есть ещё 2 попытки. Введите любую букву алфавита, чтобы разгадать пароль')
            r = 'смерть'
            word = r
            new_word = ''
            for i in range(6):
                print('Попытка', i + 1, 'из 6')
                letter = input()
                k = 1
                flag = False
                for sym in word:
                    if sym == letter:
                        print('Буква нашлась на месте', k)
                        flag = True
                        new_word += sym
                    k += 1
                if flag == False:
                    print('Буква не нашлась')
            print('Попробуйте ещё разок:0/. Введите слово>.')
            new_word = input()
            if new_word == word:
                print('Пароль подошёл!')
            else:
                print('Пароль не подошёл')
                print('У вас есть шанс. У вас опять 3 попытки>>.')
        else:
            print('Молодец, ты нашёл пароль!')
            break
else:
    print('Игра закончена<>.')

print('Вы хотите продолжить игру?')
ich = input()
if ich =='ДА' or ich == 'Да' or ich == 'дА' or ich =='да' or ich == 'конечно' or ich == 'Конечно' or ich =='КОНЕЧНО':
    print('УПС... Игра устала. Запустите её заново:>.')
else:
    print('Игра закончена<>.')
