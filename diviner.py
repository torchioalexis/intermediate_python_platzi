import random

def run():
    random_number = random.randint (1, 100)
    choose_number = input("Elige un número del 1 al 100: ")
    assert choose_number.isnumeric(), 'Tienes que ingresar un número'
    life = 5
    while int(choose_number) != random_number:
            if life == 0:
                print ("¡GAME OVER!")
                break
            print ("Tienes", life, "vida/s.")
            if random_number > int(choose_number):
                print ("Elige un número mayor")
            else:
                print ("Elige un número menor")
            choose_number = int(input("Elige otro número: "))
            life -=1
    if int(choose_number) == random_number:
        print ("¡GANASTE!")

if __name__ == "__main__":
    run()

