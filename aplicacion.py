def validar_credenciales(login, clave):
    with open("usuarios.txt", "r") as file_login, open("claves.txt", "r") as file_clave:
        logins = file_login.read().splitlines()
        claves = file_clave.read().splitlines()
        if login in logins and clave in claves:
            return True
        else:
            return False

def listar_productos():
    try:
        with open("codigo.txt", "r") as file_codigo, open("nombre.txt", "r") as file_nombre, open("precio.txt", "r") as file_precio:
            codigos = file_codigo.read().splitlines()
            nombres = file_nombre.read().splitlines()
            precios = file_precio.read().splitlines()
            if len(codigos) == len(nombres) == len(precios):
                print("Datos de los productos:")
                print("CÓDIGO\t\tNOMBRE\t\tPRECIO")
                for i in range(len(codigos)):
                    print(f"{codigos[i]}\t\t{nombres[i].ljust(15)}\t\t{precios[i]}")
            else:
                print("Error: Los archivos de datos no tienen la misma cantidad de registros.")
    except FileNotFoundError:
        print("Error: No se encontraron los archivos necesarios.")

def agregar_producto(codigo, nombre, precio):
    try:
        with open("codigo.txt", "a") as file_codigo, open("nombre.txt", "a") as file_nombre, open("precio.txt", "a") as file_precio:
            file_codigo.write(codigo + "\n")
            file_nombre.write(nombre + "\n")
            file_precio.write(precio + "\n")
        print("Producto agregado exitosamente.")
    except IOError:
        print("Error al escribir en los archivos.")

def mostrar_menu():
    while True:
        print("Menú:")
        print("1. Listar productos")
        print("2. Agregar productos")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            listar_productos()
        elif opcion == "2":
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            precio = input("Ingrese el precio del producto: ")
            agregar_producto(codigo, nombre, precio)
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def main():
    intentos = 0
    while intentos < 3:
        login = input("Ingrese su login: ")
        clave = input("Ingrese su clave: ")
        if validar_credenciales(login, clave):
            print("Bienvenido al programa.")
            mostrar_menu()
            break
        else:
            print("Usuario o contraseña incorrectos. Intente nuevamente.")
            intentos += 1
    else:
        print("Ha excedido el número de intentos permitidos. El programa terminará.")

if __name__ == "__main__":
    main()