import msvcrt
import numpy as np
import time as tm

sala=np.zeros((10,10),int)

precio_platinum=120000
precio_gold=80000
precio_silver=50000

contador_platinum=0
contador_gold=0
contador_silver=0
contador_total=0

acum_platinum=0
acum_gold=0
acum_silver=0
total_dia=0

lista_ruts=[]
lista_filas=[]
lista_columnas=[]

aux_fila=[1,2,3,4,5,6,7,8,9,10]
aux_columna=[1,2,3,4,5,6,7,8,9,10]



def mostrar_menu():
    print("""
    1. Comprar entradas
    2. Ver ubicaciones disponibles
    3. Ver listado de asistentes
    4. Mostrar ganancias totales
    5. Salir
    """)

def validar_menu():
    while True:
        try:
            opc=int(input("Ingrese una opción: "))
            if opc in (1,2,3,4,5):
                return opc
            else:
                print("ERRROR! Debe ingresar una opción válida!")    
        except:
            print("ERROR! Debe ingresar un número entero!")

def validar_rut():
    while True:
        try:
            rut=int(input("Ingrese su rut sin puntos ni dígiito verificador: "))
            if rut >=1000000 and rut<=99999999:
                return rut
            else:
                print("ERRROR! Debe ingresar un rut valido!")
        except:
             print("ERROR! Debe ingresar un número entero!")


def mostrar_sala():
    for x in range(10):
        print("fila",x+1,end="\t")
        for y in range(10):
            print(sala[x][y], end=" ")
        print(" ")

def validar_fila():
     while True:
        try:
            fila=int(input("Ingrese una fila: "))
            if fila in (1,2,3,4,5,6,7,8,9,10):
                return fila
            else:
                print("ERRROR! Debe ingresar una fila válida!")    
        except:
            print("ERROR! Debe ingresar un número entero!")

def validar_columna():
     while True:
        try:
            columna=int(input("Ingrese una columna: "))
            if columna in (1,2,3,4,5,6,7,8,9,10):
                return columna
            else:
                print("ERRROR! Debe ingresar una columna válida!")    
        except:
            print("ERROR! Debe ingresar un número entero!")

def validar_entrada():
     while True:
        try:
            entrada=int(input("Ingrese una cantidad de entradas (de 1 a 3): "))
            if entrada in (1,2,3):
                return entrada
            else:
                print("ERRROR! Mínimo 1, máximmo 3!")    
        except:
            print("ERROR! Debe ingresar un número entero!")   

def validar_tipo_entrada():
     while True:
        try:
            print("""
            1. Platinum(Fila 1 y 2):$120.000
            2. Gold(fila 3-5):  $80.000
            3. Silver(5-10):$50.000
            """)
            tipo_entrada=int(input("Ingrese un tipo de entrada: "))
            if tipo_entrada in (1,2,3):
                return tipo_entrada
            else:
                print("ERRROR! Opción inválida!")    
        except:
            print("ERROR! Debe ingresar un número entero!")                      

def comprar_entradas():
   while True: 
    rut=validar_rut()
    entrada=validar_entrada()
    mostrar_sala()
    tipo_entrada=validar_tipo_entrada()

    if tipo_entrada==1:
        total=entrada*120000
        acum_platinum=+total
        contador_platinum=+entrada
        
    elif tipo_entrada==2: 
        total=entrada*80000
        acum_gold=+total
        contador_gold=+entrada
           
    elif tipo_entrada==3:
        total=entrada*50000
        acum_silver=+total
        contador_silver=+entrada
       
    total_dia=acum_silver+acum_platinum+acum_gold
    contador_total=contador_platinum+contador_gold+contador_silver
    
    lista_ruts.append(rut)
 
def ver_asistentes():
    print(lista_ruts)

def ver_ganancias():
    print(f"""
    Tipo entrada  | Cantidad | Total
    Platinum \t \t {contador_platinum} \t {acum_platinum}
    Gold \t \t {contador_gold} \t {acum_gold}
    Silver \t \t {contador_silver} \t {acum_silver}
    ______________________________________________
    TOTAL: \t \t {contador_total} \t {total_dia}
    """)

    tm.time()

def salir():
    print("Martin Godoy 06/07/2023")        
    



