import random


def randBinary():
    r = random.random()
    print(r)

    if r < 0.5:
        print("False")
    else:
        print("True")


def findBiggerRand():
    numb1 = random.randint(0, 9999)
    numb2 = random.randint(0, 9999)

    if numb1 > numb2:
        print(f"{numb1} is bigger than {numb2}")
    elif numb2 > numb1:
        print(f"{numb2} is bigger than {numb1}")
    else:
        print(f'Numbers are equal')


def findBiggerNumberUI():
    numb1 = int(input('Enter the first Number'))
    numb2 = int(input('Enter the second Number'))

    if numb1 > numb2:
        print(f"{numb1} is bigger than {numb2}")
    elif numb2 > numb1:
        print(f"{numb2} is bigger than {numb1}")
    else:
        print(f'Numbers are equal')


def diceFenerbahceGalatasaray():
    FBW = 0
    GSW = 0
    draw = 0
    i = 0
    while i <= 1000000:
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 % 2 == 0 and dice2 % 2 == 0:
            print("Galatasaray is going to win.(even)")
            GSW = GSW + 1
        elif dice1 % 2 == 1 and dice2 % 2 == 1:
            print("Fenerbahçe is going to win.(odd)")
            FBW = FBW + 1
        else:
            print("The match is going to end on a draw.(One dice is 1 and the other is 0.)")
            draw = draw + 1
        i = i + 1

    print(f"In the moments this program run FB winned = {FBW}, GS winned = {GSW} and draw is = {draw} ")


diceFenerbahceGalatasaray()
