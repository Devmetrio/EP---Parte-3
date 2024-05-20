"""
HUERTA VASQUEZ, JIMMY ALEXANDER

Spyder Editor

This is a temporary script file.
"""

usuario = open("usuarios.txt", "rt")
verificarUsuario=usuario.read()
contrasena = open("claves.txt", "rt")
verificarContrasena=contrasena.read()

intentos=0
while intentos<3:
    user = input("\nIngresar su nombre de usuario: ")
    password = input("Ingresar su contraseña: ")
    if user==verificarUsuario and password==verificarContrasena:
        print("Datos Producto")
        print("1. Listar")
        print("2. Agregar")
        print("3. Salir")
        intentos+=3
    else:
        print("\n[El usuario y/o clave es incorrecto]")
        intentos+=1