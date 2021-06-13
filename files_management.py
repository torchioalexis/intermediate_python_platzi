import os

def read():
    names = []
    with open("./files/name.txt", "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0:
                names.append(line.strip())
    if len(names)> 0:
        print(names)
    else:
        print("Archivo vacio")

def write():
    names = []
    with open("./files/name.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

def agregar_nombre(nombre):
    with open("./files/name.txt", "a" , encoding="utf-8") as f:
        f.write(nombre)
        f.write("\n")

def borrar_nombre(nombre):
    names = []
    with open("./files/name.txt", "r", encoding="utf-8") as f:
        for line in f: 
            if len(line.strip()) > 0 and line.strip()!= nombre:
                names.append(line.strip())
    with open("./files/name.txt", "w" , encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write('\n')

    
def run():
    sw = True
    while sw:
        try:
            print("""  
----------------------------------------------------------------------
            Seleccione un numero:
            1. Crear un nuevo archivo 
            2. Agregar nombre
            3. Listar nombre
            4. Borrar nombre
            5. Salir del programa
----------------------------------------------------------------------
            """)
            n = int(input("Ingrese una opcion :   "))
            if n == 1:
                write()
            elif n == 2:
                nombre = input("Ingrese el nombre a agregar: ")
                agregar_nombre(nombre)
                os.system("clear")
                print ("¡AGREGADO!")
            elif n == 3:
                os.system("clear")
                read()
            elif n == 4:
                nombre = input("Ingrese el nombre a borrar : ")
                borrar_nombre(nombre)
                os.system("clear")
                print("¡BORRADO!")
            elif n ==5:
                sw = False
                os.system("clear")
                print("¡PROGRAMA TERMINADO, HASTA LUEGO!")
        except ValueError :
                print("Error seleccione una opcion correcta")

if __name__ == '__main__':
    run()