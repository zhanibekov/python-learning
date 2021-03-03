name = input("Как тебя зовут?")
while name!="":
    for x in range(5):
        print(name,end=" ")
    print()
    name = input("Введите ещё имя или нажмите [Enter],чтобы выйти:")
print("poshel nahoi")