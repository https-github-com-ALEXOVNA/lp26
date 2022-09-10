def cut_cake(people):
    try:
        z = 1/ people
        print(f'Everybody will get {z} - part of cake')
    except (ZeroDivisionError, TypeError):
        print('ZeroDevisionExceprion or TypeError')


cut_cake(people='0')