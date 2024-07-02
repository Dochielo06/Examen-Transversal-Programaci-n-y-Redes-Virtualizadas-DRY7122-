integrantes_grupo = [
    ('Nicolas', 'Sanchez')
]

def imprimir_integrantes(integrantes):
    for nombre, apellido in integrantes:
        print(f'{nombre} {apellido}')

imprimir_integrantes(integrantes_grupo)