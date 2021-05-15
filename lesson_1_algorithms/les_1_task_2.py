"""Пользователь вводит номер буквы в алфавите. Определить, какая это буква."""

x = int(input("введите номер буквы в алфавите (от 97 до 122): "))

if x >= 110:
    if x >= 116:
        if x >= 120:
            if x == 122:
                print('z')
            elif x == 121:
                print('y')
            else:
                print('x')
        elif x >= 118:
            if x == 119:
                print('w')
            else:
                print('v')
        elif x == 117:
            print('u')
        else:
            print('t')
    elif x >= 114:
        if x == 115:
            print('s')
        else:
            print('r')
    elif x >= 112:
        if x == 113:
            print('q')
        else:
            print('p')
    elif x == 111:
        print('o')
    else:
        print('n')
elif x >= 103:
    if x >= 107:
        if x == 109:
            print('m')
        elif x == 108:
            print('l')
        else:
            print('k')
    elif x >= 105:
        if x == 106:
            print('j')
        else:
            print('i')
    elif x == 104:
        print('h')
    else:
        print('g')
elif x >= 101:
    if x == 102:
        print('f')
    else:
        print('e')
elif x >= 99:
    if x == 100:
        print('d')
    else:
        print('c')
elif x == 98:
    print('b')
else:
    print('a')
