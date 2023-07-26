
import random

animals = ['1:Tortuga','2:Perro','3:Gato','4:Abeja']
print (animals)
animal = input ()
number1 = input ()
number2 = input ()
number3 = input ()
number4 = input ()
number_lotery = (number1 + number2 + number3 + number4) 
print (number_lotery)
number_lotery1 = random.randint(1,3)
number_lotery2 = random.randint(1,3)
number_lotery3 = random.randint(1,3)
number_lotery4 = random.randint(1,3)
if number1 == number_lotery1 and number2 == number_lotery2 and number3 == number_lotery3 and number4 == number_lotery4:
  print ('Felicidades ... Ganaste la Loteria!!!!')
else:
    print("los sentimos... Sigue participando....")

animal_lotery = random.randint(1,4)
if animal == animal_lotery:
  print('Animal Ganador Boleto Gratis')
else:
  print("Sin mascota")
