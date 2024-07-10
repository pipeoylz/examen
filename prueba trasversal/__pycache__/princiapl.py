import funciones as fn

trabajadores = ['juan perez','maria gracia','carlos lopes','ana martines','pedro rodriguez','laura hernadez','miguel sanxhez','isabel gomez','francisco dias','elena hernadez']

while True:
    print("beienvendio\n0. inciazlizar creditos\n1. asignar creditos aleatorios\n2 clasificar suledos\n3. ver estadisticas\n4 reporte de sueldos\n5 salir")
    opcion = int(input("ingrese una opcion: "))

    if opcion==0:
        creditos_trabajadores = {trabajador : 0 for trabajador in trabajadores}
        print("se incialiso correctamente")

    elif opcion==1:
        if not creditos_trabajadores:
            print("primero debes inicializar los creditos")
        else:
            creditos_trabajadores = fn.asignar_sueldos(trabajadores)

    
    elif opcion==2:
        if creditos_trabajadores:
            fn.clasificar_sueldos(creditos_trabajadores)
        else:
            print("primero debes inicializar los sueldos")
    elif opcion==3:
        if creditos_trabajadores:
            max_sueldo,min_sueldo,promedio_sueldos = fn.ver_estadistias(creditos_trabajadores)

            if max_sueldo is not None:
                print("el sueldo mayor dado es de $",max_sueldo)
                print("el sueldo minimo dado es de $",min_sueldo)
                print("el proemedio de los sueldos dados es de $",promedio_sueldos)
        else:
            print("primero debes asignar los sueldos")
    elif opcion==4:
        if creditos_trabajadores:
            fn.reporte_sueldos(creditos_trabajadores)
        else:
            print("primero debe asignar los sueldos")
    elif opcion==5:
        print("espero que tenga un buen dia")
        print("Finalizando programa…")
        print("desarrollado por felipe oyarzo")
        print("rut 21839591-0")
        break
    else:
        print("desbes asignar un numero entre el 0 y 5 porfavor")
