from time import sleep
n1 = int(input('First number: '))
n2 = int(input('Second number: '))
option = 0
while option != 7:
    print(''' \t [ 1 ] Sum
     [ 2 ] Subtract
     [ 3 ] Multiply
     [ 4 ] Division
     [ 5 ] Greater
     [ 6 ] New numbers
     [ 7 ] Exit the program''')
    option = int(input('>>>>> What is your option? '))
    if option == 1:
        sum = n1 + n2
        print('The \033[1;33mSUM\033[m between \033[1;34m{}\033[m + \033[1;35m{}\033[m it is \033[1;32m{}\033[m'.format(n1, n2, sum))
    elif option == 2:
        subtract = n1 - n2
        print('The \033[1;33mSUBTRACTION\033[m between \033[1;34m{}\033[m - \033[1;35m{}\033[m it is \033[1;32m{}\033[m'.format(n1, n2, subtract))
    elif option == 3:
        multiplication = n1 * n2
        print('The \033[1;33mMULTIPLICATION\033[m between \033[1;34m{}\033[m * \033[1;35m{}\033[m it is \033[1;32m{}\033[m'.format(n1, n2, multiplication))
    elif option == 4:
        division = n1 / n2
        print('The \033[1;33mDIVISION\033[m between \033[1;34m{}\033[m / \033[1;35m{}\033[m it is \033[1;32m{}\033[m'.format(n1, n2, division))
    elif option == 5:
        if n1 > n2:
            greater = n1
        else:
            greater = n2
        print('The \033[1;33mGREATER\033[m between \033[1;34m{}\033[m and \033[1;35m{}\033[m it is \033[1;32m{}\033[m'.format(n1, n2, greater))
    elif option == 6:
        print('Type the new numbers again: ')
        n1 = int(input('First number: '))
        n2 = int(input('Second number: '))
    elif option == 7:
        print('\033[1;31mShuting down...\033[m')
    else:
        print('Invalid option. Try again')
    print('=-=' * 10)
    sleep(2)
print('\033[1;32mEnd of the program!\033[m')
