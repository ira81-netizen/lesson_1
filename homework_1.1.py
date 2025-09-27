ask1 = input('Уведіть ваше імя: ')
ask2 = int(input('Уведіть ваш вік: '))
if ask2 >= 18:
    print(f'{ask1}, вхід дозволено.')
else:
    print(f'{ask1}, вхід заборонено.')
    