import random
the_number = random.randint(1,100)
guess = int(input("УГАДАЙТЕ ЧИСЛО ОТ 1 ДО 10:"))
while guess!=the_number:
    if guess > the_number:
        print(guess,"СЛИШКОМ ВЕЛИКО.ПОПОБРУЙТЕ СНОВА.")
    if guess < the_number:
        print(guess, "СЛИШКОМ МАЛО.ПОПРОБУЙТЕ СНОВА.")
    guess = int(input("ЕЩЁ ОДНА ПОПЫТКА:"))
    print(guess,"Правильное число! ВЫ ПОБЕДИЛИ!")