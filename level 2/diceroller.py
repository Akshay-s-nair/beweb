import random
while(True):
    check=input('Enter 1 to roll the dice and 0 to exit: ')
    if check=='1':
        x=random.randrange(1,7)
        print(f"\nDice rolled with value {x}")
        y=x//2
        for i in range(y):
            print('. '*2)
        if x-y*2==1:
            print(' . ')
        print('\n')
    elif check=='0':
        print('Terminating...')
        exit()
    else:
        print('Invalid choice')