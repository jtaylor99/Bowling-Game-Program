def bowlers_turn():
    total = 0
    for frame in range(1, 11):
        print('frame', frame)
        frame = []
        for _ in range(2):
            throw = int(input('Pins:'))

            frame.append(total)
        if throw > 10:
            print('Oops! you can\'t go over 10')


def bowlers_score():
    total = 0
    frames = []
    for i in range(len(frames)):
        if '/' in frames[i]:
            ball_1 = frames[i][0]
            ball_2 = 10 - ball_1
            total += ball_1 + ball_2
            if i + 1 < len(frames):
                next_ball = frames[i + 1][0]
                total += next_ball
            elif 'x' in frames[i]:
                ball_1 = 10
                total += ball_1

            else:
                total += sum(frames[i])
    print(total)
