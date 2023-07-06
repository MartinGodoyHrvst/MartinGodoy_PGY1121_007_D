import Funciones as fn

while True:
    fn.mostrar_menu()
    opc=fn.validar_menu()
    if opc ==1:
        fn.comprar_entradas()
    elif opc==2:
        fn.mostrar_sala()
    elif opc==3:
        fn.ver_asistentes()
    elif opc==4:
        fn.ver_ganancias()    
    else:
        fn.salir()
        break