servicios_listado = {
     1: "Corte de cabello",
     2: "Corte + Barba",
     3: "Corte + Barba + Cejas",
     4: "Barba + Cejas",
}

servicios_precios = {
     1: 20000,
     2: 23000,
     3: 25000,
     4: 8000,
}

citas = []


def servicios():
    print("""
    -------------Servicios disponibles------------
    1) Corte de cabello ................. $20.000
    2) Corte + Barba .................... $23.000
    3) Corte + Barba + Cejas ............ $25.000
    4) Barba + Cejas .................... $8.000    
    ----------------------------------------------
    """)


def agendar_cita():
     print("\n------------ Agendar cita --------------")
     nombre = input("Ingrese su nombre: ")   
     print()
     servicio_opcion = 0
     while servicio_opcion not in range(1, 5):
       try:
           servicio_opcion = int(input("Seleccione el servicio (1-4): "))
           if servicio_opcion not in range(1, 5):
               print("Opción inválida, por favor elija un número entre 1 y 4.")
       except ValueError:
           print("Debe ingresar un número.")

     servicio = servicios_listado[servicio_opcion]
     precio = servicios_precios[servicio_opcion]

     print()
     fecha = input("Ingrese la fecha que desea agendar la cita (dd/mm/aaaa): ")
     print()
     hora = input("Ingrese la hora que desea el corte (HH:MM): ")
     
     print("\n Su cita se ha agendado con éxito\n")
     print(f"Cliente: {nombre}")
     print(f"Servicio: {servicio}")
     print(f"Precio: ${precio}")
     print(f"Fecha: {fecha}")
     print(f"Hora: {hora}")

     cita = {
       "nombre": nombre,
       "servicio": servicio,
       "precio": precio,
       "fecha": fecha,
       "hora": hora
      }   
     citas.append(cita)


def cancelar_cita():
    print("\n-----------------Cancelar cita--------------------")
    if not citas:
        print("No hay citas registradas")
        return
    nombre = input("Ingrese su nombre para buscar su cita: ").strip().lower()
    for cita in citas:
        if cita["nombre"].strip().lower() == nombre:
            citas.remove(cita)
            print(f"La cita de {nombre} ha sido cancelada con éxito.")
            return 
    print("No se encontró ninguna cita con ese nombre.")    


def citass():
    print("\n-----------------Citas registradas--------------------")
    if not citas:
        print("No hay citas que mostrar")
        return
    for cita in citas:
        print(f"Cliente :{cita['nombre']} - Servicio: {cita['servicio']} -Valor: ${cita['precio']} - Fecha: {cita['fecha']} a las {cita['hora']}")


def ver_ingresos():
    print("\n-----------------Ingresos totales--------------------")
    if not citas:
        print("No hay citas registradas aún")
        return
    total = sum(cita["precio"] for cita in citas)
    print(f"Ingresos acumulados: ${total}")


def menu():
    while True:
        print("""
---------------BIENVENIDO A  NUESTRA BARBERIA-----------------

  Por favor observe la opción que busca:
       
       0) Servicios disponibles
       1) Agendar cita
       2) Cancelar cita
       3) Citas programadas
       4) Salir del programa
       5) Ver ingresos totales
""")
        try:
             opcion = int(input("Ingrese la opción que requiere: "))    
             if opcion == 0:
                  servicios()
             elif opcion == 1:
                  agendar_cita()
             elif opcion == 2:
                  cancelar_cita()  
             elif opcion == 3:
                  citass()
             elif opcion == 4:
                  print("Gracias por visitar nuestra barbería. ¡Hasta luego!")
                  break
             elif opcion == 5:
                  ver_ingresos()
             else:
                  print("Opción inválida, intente de nuevo.")
        except ValueError:
            print("Ingrese un número válido")     
    
     
menu()
