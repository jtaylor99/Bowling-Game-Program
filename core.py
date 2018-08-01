from random import randint


def lane():
    ball_roll = randint(range(10))
    if ball_roll < 10:
        return 'points'
