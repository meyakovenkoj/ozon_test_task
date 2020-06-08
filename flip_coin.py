from datetime import datetime
import random


def coin():
    td = datetime.today()
    week_dict = {0: 0.5, 1: 1, 2:0.7, 3:0.5, 4:0, 5:0.4, 6:0}
    weekday = td.weekday()
    print('решка' if random.random() < week_dict[weekday] else 'орел')


if __name__ == '__main__':
    coin()
