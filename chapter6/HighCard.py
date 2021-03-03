import random
suits = ["piki","bubna", "chervi"]
faces = ["dvoika", "troyka", "chetverka", "peterka", "shesterka", "semerka", "vosmerka","devyatka", "desyatka", "valet", "dama","korol", "tuz"]
keep_going = True
while keep_going:
    my_face = random.choice(faces)
    my_suit = random.choice(suits)
    your_face = random.choice(faces)
    your_suit = random.choice(suits)
    print("У меня", my_face, "", my_suit)
    print("У ВАС", your_face, "", your_suit)
    if faces.index(my_face) > faces.index(your_face):
        print("Я победил!")
    elif faces.index(my_face) < faces.index(your_face):
        print("ВЫ ПОБЕДИЛИ!")
    else:
        print("У НАС НИЧЬЯ!")
    answer = input("Нажмите [ENTER], ЧТОБЫ ПРОДОЛЖИТЬ,ЛЮБУЮ")
    keep_going = (answer == "")
