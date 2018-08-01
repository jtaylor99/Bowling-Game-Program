import core


def main():
    print('Welcome to the Bowling Alley!')
    print('One of the best Local Bowling Alley')
    players = input('How players do you have ')
    while True:
        if players.isdigit():
            print('Ok, go to for your shoes')
            break
        else:
            print('Please choose a valid option!')


if __name__ == '__main__':
    main()
