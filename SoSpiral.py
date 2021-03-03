answer = input ("Хотите увидеть спираль? д/н:")
if answer == 'д':
    print ("работаем...")
import turtle
t = turtle.Pen()
t.width(2)
for x in range (100):
    t.forward(x*2)
    t.left(89)
    print("Ну вот,готово!")
