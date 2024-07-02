def determinar_rango_vlan(numero_vlan):
    if 1 <= numero_vlan <= 1000:
        return "VLAN del rango normal"
    elif 1002 <= numero_vlan <= 4094:
        return "VLAN del rango extendido"
    else:
        return "Numero de VLAN fuera de los rangos conocidos"

try:
    numero_vlan = int(input("Ingrese el numero de VLAN: "))
    resultado = determinar_rango_vlan(numero_vlan)
    print(f"El numero de VLAN {numero_vlan} es {resultado}.")
except ValueError:
    print("Error: Debe ingresar un numero entero para el numero de VLAN.")