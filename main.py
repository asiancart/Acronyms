NUMBER_OF_DIGITS = 10

def main():
    print('Soroban - The Japanese Abacus')
    print('By asiancart')
    print()

    abacusNumber = 0

    while True:
        displayAbacus(abacusNumber)
        displayControls()

        commands = input('> ')
        if commands == 'quit':
            break
        elif commands.isdecimal():
            abacusNumber = int(commands)
        else:
            for letter in commands:
                if letter == 'q':
                    abacusNumber += 1000000000
                elif letter == 'a':
                    abacusNumber -= 1000000000
                elif letter == 'w':
                    abacusNumber += 100000000
                elif letter == 's':
                    abacusNumber -= 100000000
                elif letter == 'e':
                    abacusNumber += 10000000
                elif letter == 'd':
                    abacusNumber -= 10000000
                elif letter == 'r':
                    abacusNumber += 1000000
                elif letter == 'f':
                    abacusNumber -= 1000000
                elif letter == 't':
                    abacusNumber += 100000
                elif letter == 'g':
                    abacusNumber -= 100000
                elif letter == 'y':
                    abacusNumber += 10000
                elif letter == 'h':
                    abacusNumber -= 10000
                elif letter == 'u':
                    abacusNumber += 1000
                elif letter == 'j':
                    abacusNumber -= 1000
                elif letter == 'i':
                    abacusNumber += 100
                elif letter == 'k':
                    abacusNumber -= 100
                elif letter == 'o':
                    abacusNumber += 10
                elif letter == 'l':
                    abacusNumber -= 10
                elif letter == 'p':
                    abacusNumber += 1
                elif letter == ';':
                    abacusNumber -= 1

        if abacusNumber < 0:
            abacusNumber = 0

        if abacusNumber >  9999999999:
            abacusNumber = 9999999999

def displayAbacus(number):
    numberList = list(str(number).zfill((NUMBER_OF_DIGITS)))

    hasBead = []

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01234')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '56789')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '0123456789')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '234789')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '034589')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '014569')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '012567')

    for i in range(NUMBER_OF_DIGITS):
        hasBead.append(numberList[i] in '01235678')

    abacusChar = []
    for i, beadPresent in enumerate(hasBead):
        if beadPresent:
            abacusChar.append('0')
        else:
            abacusChar.append('|')

    chars = abacusChar + numberList
    print(''' 
    +================================+
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  |  |  |  |  |  |  |  |  |  |  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    +================================+
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
    +=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+'''.format(*chars))


def displayControls():
    print(' +q w e r t y u i o p')
    print(' -a s d f g h j k l ;')
    print('(Enter a number, "quit", or a stream of up/down letters.)')

if __name__ == '__main__':
    main()