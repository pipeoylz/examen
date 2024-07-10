import random
import csv







def asignar_sueldos(trabajadores):

    
    creditos_trabajadores = {}

    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        creditos_trabajadores[trabajador] = sueldo
    print("creditos asignados correctamente")
    print(creditos_trabajadores)
    return(creditos_trabajadores)


def clasificar_sueldos(creditos_trabajadores):
    menor_800000 = {}
    entre_800000_2000000 = {}
    mayor_2000000 = {}

    for trabajador,sueldo in creditos_trabajadores.items():
        if sueldo < 800000:
            menor_800000[trabajador] = sueldo
        elif sueldo <= 2000000:
            entre_800000_2000000[trabajador] = sueldo
        else:
            mayor_2000000[trabajador] = sueldo
        
    print("los sueldos menores a $ 800000 es TOTAL",len(menor_800000))
    for trabajador,sueldo in menor_800000.items():
        print(trabajador,': $',sueldo)

    print("los sueldos entre $800000 y $2000000  es TOTAL",len(entre_800000_2000000))
    for trabajador,sueldo in entre_800000_2000000.items():
        print(trabajador,': $',sueldo)

    print("los sueldos mayores a $2000000 son TOTAL",len(mayor_2000000))
    for trabajador,sueldo in mayor_2000000.items():
        print(trabajador,': $',sueldo)

        


def ver_estadistias(creditos_trabajadores):
    sueldos = list(creditos_trabajadores.values())

    if not creditos_trabajadores:
        print("primero debes inicializar los creditos")
        return None,None,None
    
    max_sueldo = max(sueldos)
    min_sueldo = min(sueldos)
    promedio_sueldos = sum(sueldos) / len(sueldos)

    return max_sueldo,min_sueldo,promedio_sueldos


def reporte_sueldos(creditos_trabajadores):
    with open('reporte_sueldos.csv', 'w', newline='') as archivo:
        escritor = csv.writer(archivo)
        
        escritor.writerow(['nombre trabajador', 'sueldo base', 'descuento salud', 'descuento afp', 'sueldo liquido'])
        
        for trabajador, sueldo in creditos_trabajadores.items():
            
            descuentosalud = sueldo * 0.07  
            descuentoafp = sueldo * 0.12   
            liquidoapagar = sueldo - descuentoafp - descuentosalud
            
            
            escritor.writerow([trabajador, sueldo, descuentosalud, descuentoafp, liquidoapagar])
    
    print("Reporte generado exitosamente en reporte_sueldos.csv")




    




    

