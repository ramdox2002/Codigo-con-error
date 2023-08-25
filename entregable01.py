# Descuento por compras mayores a 100 soles del 5%
# El valor esta en dolares asi que lo convertire a soles
from datetime import datetime

global hora_actual, fecha_actual

# Obtener la fecha actual
fecha_actual = datetime.now().date()

# Obtener la hora actual
hora_actual = datetime.now().time()

data = [
    {
        "id": 1,
        "nombre": "Martillo",
        "precio": 12.99,
        "categoria": "Herramientas",
        "stock": 50
    },
    {
        "id": 2,
        "nombre": "Tornillos",
        "precio": 0.99,
        "categoria": "Fijaciones",
        "stock": 500
    },
    {
        "id": 3,
        "nombre": "Destornillador",
        "precio": 6.49,
        "categoria": "Herramientas",
        "stock": 75
    },
    {
        "id": 11,
        "nombre": "Pintura",
        "precio": 19.99,
        "categoria": "Pinturas",
        "stock": 30
    },
    {
        "id": 12,
        "nombre": "Cinta Métrica",
        "precio": 3.75,
        "categoria": "Herramientas",
        "stock": 40
    }
]

cl = input("Ingrese su nombre: ")
mp = input("Metodo de Pago: ")
DNI = input("Ingrese su DNI: ")
producto:int = input("Ingrese el producto: ")
unidades:int = int(input("Cuantas unidades se va a llevar: "))

aux = False

while not aux:
    for i in data:
        if i["nombre"] == producto:

            PEN = i["precio"] * 3.73
            UxP = unidades * PEN
            if unidades >=  100:
                descuento = (UxP / 100) * 5

                IGV = (UxP / 100) * 18
                total = UxP + IGV - descuento
                
                response = input("Desea generar una boleta yes/no: ").lower()
                if response == "yes":
                    print("""
-------------------------------------
:::::::::Ferretería Leonardo:::::::::
::---------------------------------::
:: Datos                           ::
::---------------------------------::
:: Fecha: %s               ::
:: Hora : %s          ::
::---------------------------------::
:: Cajero        : %s         ::
:: Cliente       : %s        ::
:: DNI           : %s       ::
:: Metodo de Pago: %s         ::
::---------------------------------::
:: Operaciones                     ::
::---------------------------------::
:: Precio del Producto: %s      ::
:: IGV                : %s     ::
:: Descuento          : %s     ::
:: Total              : %s    ::
-------------------------------------
                          """ %(fecha_actual, hora_actual, "unknown", cl, DNI, mp, str(i["precio"]), str(round(IGV, 2)), str(round(descuento, 2)), str(round(total, 2))))
                    aux = True
                elif response == "no":
                    aux = True
                else:
                    print("Selecione una opcion valida")
                    aux = True
            else:
                print("No tiene DESCUENTO")
                # PROCEDE A COBRAR SIN DESCUENTO

                IGV = (UxP / 100) * 18
                total = UxP + IGV
                response = input("Desea generar una boleta yes/no: ").lower()
                if response == "yes":
                    print("""
-------------------------------------
:::::::::Ferretería Leonardo:::::::::
::---------------------------------::
:: Datos                           ::
::---------------------------------::
:: Fecha: %s               ::
:: Hora : %s          ::
::---------------------------------::
:: Cajero        : %s         ::
:: Cliente       : %s        ::
:: DNI           : %s       ::
:: Metodo de Pago: %s         ::
::---------------------------------::
:: Operaciones                     ::
::---------------------------------::
:: Precio del Producto: %s      ::
:: IGV                : %s     ::
:: Descuento          : 0     ::
:: Total              : %s    ::
-------------------------------------
                          """ %(fecha_actual, hora_actual, "unknown", cl, DNI, mp, str(i["precio"]), str(round(IGV, 2)), str(round(total, 2))))
                    aux = True
                elif response == "no":
                    aux = True
                else:
                    print("Selecione una opcion valida")
                    aux = True

        else:
            if i["nombre"] == producto:
                # print("No contamos con ese producto: %s" %(producto))
                exit()
            else:
                print("No contamos con ese producto: %s" %(producto))
                exit()