#Ejercicio 1 - Condicionales
age = int(input("Buenos días. ¿Su edad por favor? "))
if (age > 110 or age < 0):
    print("Con esa edad, ¿está usted vivo?")
elif (age >= 18):
    print("Puede pasar, adelante.")
else:
    print("Lo siento pero no puede pasar.")