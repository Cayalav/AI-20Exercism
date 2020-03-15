TOTAL_ROLLS = 5


def yacht(dice):
    for a in dice:
        if dice.count(a) == TOTAL_ROLLS:
            return 50
    return 0


def _count_of_number_times_number(integer, dice):
    if len(dice) != TOTAL_ROLLS:		# only 5 dice
        return 0
    return integer * dice.count(integer)	#return dice number * quinaty


def ones(dice):
    return _count_of_number_times_number(1, dice)


def twos(dice):
    return _count_of_number_times_number(2, dice)


def threes(dice):
    return _count_of_number_times_number(3, dice)


def fours(dice):
    return _count_of_number_times_number(4, dice)


def fives(dice):
    return _count_of_number_times_number(5, dice)


def sixes(dice):
    return _count_of_number_times_number(6, dice)


def full_house(dice):
    threes = 0
    for a in dice:
        if dice.count(a) == 3:
            threes = a
    if threes == 0:
        return 0
    twos = 0
    for a in dice:
        if dice.count(a) == 2:
            twos = a
    if twos == 0:
        return 0
    return 3 * threes + 2 * twos


def four_of_a_kind(dice):
    for a in dice:
        count_of_roll = dice.count(a)
        if count_of_roll in (4, 5):
            return 4 * a
    return 0


def litte_straight(dice):
    if dice == [1, 2, 3, 4, 5]:
        return 30
    return 0


def big_straight(dice):
    if dice == [2, 3, 4, 5, 6]:
        return 30
    return 0


def choice(dice):
    sum = 0
    for a in dice:
        sum += a
    return sum

# function names from test
YACHT = yacht
ONES = ones
TWOS = twos
THREES = threes
FOURS = fours
FIVES = fives
SIXES = sixes
FULL_HOUSE = full_house
FOUR_OF_A_KIND = four_of_a_kind
LITTLE_STRAIGHT = litte_straight
BIG_STRAIGHT = big_straight
CHOICE = choice


def score(dice, category):
    return category(sorted(dice)) # dice[],Function Call()

