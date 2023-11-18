import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    if random.randint(1, 10) == 1:
        error = random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
        raise error("Bad karma error!")
    return random.randint(1, 7)


karma = 0
with open('karma.log', 'a') as f:
    while karma < 500:
        try:
            karma += one_day()
        except Exception as e:
            f.write(str(e) + '\n')
