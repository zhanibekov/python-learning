rainy = input("КАК ПОГОДКА? ИДЁТ ДОЖДЬ? (Y/N) ").lower()
cold = input("НА УЛИЦЕ ХОЛОДНО? (Y/N) ").lower()
if (rainy == 'Y' and cold == 'Y'):
    print("ЛУЧШЕ НАДЕНЬТЕ ПЛАЩ.")
elif (rainy == 'Y' and cold!= 'Y'):
    print("ВОЗМИТЕ С СОБОЙ ЗОНТ!")
elif (rainy!= 'Y' and cold == 'Y' ):
    print("НАДЕНЬТЕ ПАЛЬТО: НА УЛИЦЕ ХОЛОДНО!")
elif (rainy!= 'Y' and cold!= 'Y'):
    print("НАДЕВАЙТЕ, ЧТО ХОТИТЕ: НА УЛИЦЕ ПРЕКРАСНО!")
