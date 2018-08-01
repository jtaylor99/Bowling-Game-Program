import core


def main():
    print('Welcome to the Bowling Alley!')
    print('One of the best Local Bowling Alley')
    while True:
        players = input('How players do you have:')
        if players.isdigit():
            print(
                'Ok, go to the next counter your shoes and you are on lane 1')
            break
        else:
            print('Please choose a valid option!')
    while True:
        size = input('What is the size of your shoe:')
        if size.isdigit():
            print('Ok here you go and enjoy your game')
            break
        else:
            print('Please choose a valid option!')
    user_name = input('Please type your name:')

    print('Let\'s begin')
    total = 0
    frames = []
    while True:
        for frame in range(1, 11):
            print('frame', frame)
            frame = []
            for _ in range(2):
                throw = int(input('Pins:'))
                if throw == 0:
                    print('That\'s a Gutter!!!!!')
                if throw > 10:
                    print('Please don\'t go over 10')

            frame.append(throw)
            total += sum(frame)
        frames.append(total)

    print(frames)


if __name__ == '__main__':
    main()
