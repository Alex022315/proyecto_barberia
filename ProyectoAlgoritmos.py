import re
from datetime import datetime
import winsound

# Funciones para los sonidos
def correcto():
    winsound.Beep(440, 1000)

def incorrecto():
    winsound.Beep(800, 1000)

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
    print("""\n------------ Agendar cita --------------
    Horarios de atención L-D de 9 am a 20 pm""")
    while True:
        nombre = input("Ingrese su nombre y apellido: ").strip()
        if not re.match("^[a-zA-Z\s]+$", nombre) or len(nombre) < 2:
            print("🚫 Ingrese un nombre válido (solo letras y al menos 2 caracteres).")
            incorrecto()
        else:
            break
            
    servicios() #vuelve a llamar los servicios disponibles
    servicio_opcion = 0
    while servicio_opcion not in range(1, 5):
        try:
            servicio_opcion = int(input("Seleccione el servicio (1-4): "))
            if servicio_opcion not in range(1, 5):
                print("Opción inválida, por favor elija un número entre 1 y 4.")
                incorrecto()
        except ValueError:
            print("Debe ingresar un número.")
            incorrecto()

    servicio = servicios_listado[servicio_opcion]
    precio = servicios_precios[servicio_opcion]

    # En este bloque de código validamos la fecha.
    while True:
        fecha_str = input("Ingrese la fecha que desea agendar la cita (dd-mm-aaaa): ")
        try:
            fecha_cita = datetime.strptime(fecha_str, '%d-%m-%Y').date()
            if fecha_cita < datetime.now().date():
                print("🚫 Ingrese una fecha válida, no puede ser una fecha anterior a la actual.")
                incorrecto()
            else:
                break
        except ValueError:
            print("🚫 Ingrese una fecha válida en formato dd-mm-aaaa.")
            incorrecto()
    # F
            
    # En este bloque validamos la hora.
    while True:
        hora_str = input("Ingrese la hora (Formato de 24 horas HH:MM): ")
        try:
            hora_cita = datetime.strptime(hora_str, '%H:%M').time()
            hora_min = datetime.strptime('09:00', '%H:%M').time()
            hora_max = datetime.strptime('20:00', '%H:%M').time()
            
            # condicional para validar el rango según horario de atención
            if not (hora_min <= hora_cita <= hora_max):
                print("🚫 Ingrese una hora válida, el horario de atención es de 09:00 a 20:00.")
                incorrecto()
            # Si la fecha es la actual, valida que la hora no sea anterior a la hora actual
            elif fecha_cita == datetime.now().date() and hora_cita < datetime.now().time():
                 print("🚫 No puede agendar una hora anterior a la actual.")
                 incorrecto()
            else:
                break
        except ValueError:
            print("🚫 Ingrese una hora válida en formato HH:MM.")
            incorrecto()

    # Con un for recorro las citas para validar que no exista una cita con la misma fecha y hora.
    for cita_existente in citas:
        if cita_existente['fecha'] == fecha_str and cita_existente['hora'] == hora_str:
            print("🚫 Ya existe una cita agendada para esta fecha y hora. Por favor, elija otra.")
            incorrecto()
            return

    cita = {
        "nombre": nombre,
        "servicio": servicio,
        "precio": precio,
        "fecha": fecha_str,
        "hora": hora_str
    }
    citas.append(cita)
    
    print("\n✅ Su cita se ha agendado con éxito\n")
    print(f"Cliente: {nombre.title()}")
    print(f"Servicio: {servicio}")
    print(f"Precio: ${precio}")
    print(f"Fecha: {fecha_str}")
    print(f"Hora: {hora_str}")
    correcto()


def cancelar_cita():
    print("\n-----------------Cancelar cita--------------------")
    if not citas:
        print("No hay citas registradas.")
        return
    
    while True:
        nombre = input("Ingrese su nombre y apellido para buscar su cita: ").strip().lower()
        
        cita_encontrada = False
        for cita in citas:
            if cita["nombre"].strip().lower() == nombre:
                citas.remove(cita)
                print(f"✅ La cita de {nombre.title()} ha sido cancelada con éxito.")
                correcto()
                cita_encontrada = True
                break
        
        if cita_encontrada:
            break
        else:
            print("❌ No se encontró ninguna cita con ese nombre.")
            incorrecto()
            opcion = input("¿Desea intentarlo de nuevo? (s/n): ").strip().lower()
            if opcion != 's':
                break


def citass():
    print("\n-----------------Citas registradas--------------------")
    if not citas:
        print("No hay citas que mostrar.")
        return
    for cita in citas:
        print(f"Cliente: {cita['nombre'].title()} - Servicio: {cita['servicio']} - Valor: ${cita['precio']} - Fecha: {cita['fecha']} a las {cita['hora']}")


def ver_ingresos():
    print("\n-----------------Ingresos totales--------------------")
    if not citas:
        print("No hay citas registradas aún.")
        return
    total = sum(cita["precio"] for cita in citas)
    print(f"Ingresos acumulados: ${total}")


def menu():
    while True:
        print("""
---------------BIENVENIDO A  NUESTRA BARBERÍA-----------------
Por favor observe la opción que busca:
        
    0) Servicios disponibles
    1) Agendar cita
    2) Cancelar cita
    3) Citas programadas
    4) Ver ingresos totales
    5) Salir del programa
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
                ver_ingresos()
            elif opcion == 5:
                print("Gracias por visitar nuestra barbería. ¡Hasta luego!")
                correcto()
                break
            else:
                print("Opción inválida, intente de nuevo.")
                incorrecto()
        except ValueError:
            print("Ingrese un número válido.")  
            incorrecto()
    
menu()
