#  CALCULADORA BASICA

print("Si no sabes hacer operaciones aritmeticas como yo >:) ")

def suma(x,y):
    global z
    z=x+y
    return(z)

def resta(x,y):
    global z
    z=x-y
    return(z)

def multiplicacion(x,y):
    global z
    z=x*y
    return(z)

def division(x,y):
    global z
    try:
        z=x/y
        return(z)
    except ZeroDivisionError:
        print("No seas bobo, no se puede dividir entre 0")

def potencia(x,y):
    global z
    z=x**y
    return(z)    

def operaciones():
     global z
     print("Operaciones\n")
     print("1) Suma\n")
     print("2) Resta\n")
     print("3) Multiplicacion\n")
     print("4) Division\n")
     print("5) Potencia\n")
     print("99) Salir\n")
     opcion = int(input("Selecciona el procedimiento aritmetico que quieras usar owo: "))
     while(opcion>0 and opcion<99):
          x = float(input("Ingresa el primer digito: "))
          y = float(input("Ingresa el segundo digito: "))
          if (opcion==1):
               suma(x,y)
          elif (opcion==2):
               resta(x,y)
          elif (opcion==3):
               multiplicacion(x,y)
          elif (opcion==4):
               division(x,y)
          elif (opcion==5):
            potencia(x,y)
        
          print("El resultado es: ",z)     
          opcion=int(input("Selecciona el procedimiento aritmetico que quieras usar owo: "))
operaciones() 
