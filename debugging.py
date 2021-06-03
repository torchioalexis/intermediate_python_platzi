def divisor (num):
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run ():
    try:
        num = int(input("Ingresa un número: "))
        if num < 0:
            raise ValueError("No se puede ingresar un número menor a 0")
        print (divisor(num))
        print ("Termina mi programa")
    except ValueError:
        print ("Debes ingresar un número entero positivo")
        run()

if __name__ == "__main__":
    run ()