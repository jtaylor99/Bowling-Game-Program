import core


def main():
    print('Welcome to the Bowling Alley!')
    print('Let\'s begin')
    frames = []
    for frame in range(1, 11):
        print('frame', frame)
        frame = []
        for _ in range(2):
            throw = int(input('Pins:'))
            frame.append(throw)
        frames.append(frame)

    print(frames)


if __name__ == '__main__':
    main()
