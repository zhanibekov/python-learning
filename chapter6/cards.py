import random
faces = ["Двойка","troyka", "chetverka", "peterka", "shesterka", "semerka", "vosmerka","devyatka", "desyatka", "valet", "dama","korol", "tuz"]
my_face = random.choice(faces)
your_face = random.choice(faces)

print(my_face)
print(your_face)
print('============')
print(faces.index(my_face))
print(faces.index(your_face))
if faces.index(my_face) > faces.index(your_face):
    print("Я победил!")
elif faces.index (my_face) < faces.index(your_face):
    print("Вы победили!")
else:
    print("НИЧЬЯ!")
