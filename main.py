import conciertos

concierto1 = conciertos.Concierto('Rosalía', 'Madrid', 60.0, 100)
concierto2 = conciertos.Concierto('Estopa', 'Barcelona', 35.0, 80)
concierto3 = conciertos.Concierto('Melendi', 'Sevilla', 50.0, 50)

usuario1 = conciertos.Usuario('Ana', 20)
usuario2 = conciertos.Usuario('Luis', 25)
usuario3 = conciertos.Usuario('Marta', 35)

usuario1.comprar_entrada(concierto1, 'pista')
usuario1.comprar_entrada(concierto2, 'vip')
usuario2.comprar_entrada(concierto1, 'grada')
usuario2.comprar_entrada(concierto3, 'pista')
usuario3.comprar_entrada(concierto1, 'pista')
usuario3.comprar_entrada(concierto2, 'grada')

usuario1.valorar(concierto1, 9)
usuario2.valorar(concierto3, 7)
usuario3.valorar(concierto2, 8)

lista_conciertos = [concierto1, concierto2, concierto3]

total_entradas = 0
for concierto in lista_conciertos:
    total_entradas += len(concierto.entradas_vendidas)
print(f'Entradas vendidas en total: {total_entradas}')

entradas_pista = 0
entradas_grada = 0
entradas_vip = 0
for concierto in lista_conciertos:
    for entrada in concierto.entradas_vendidas:
        if isinstance(entrada, conciertos.EntradaPista):
            entradas_pista += 1
        elif isinstance(entrada, conciertos.EntradaGrada):
            entradas_grada += 1
        elif isinstance(entrada, conciertos.EntradaVIP):
            entradas_vip += 1
print(f'Entradas de pista vendidas: {entradas_pista}')
print(f'Entradas de grada vendidas: {entradas_grada}')
print(f'Entradas VIP vendidas: {entradas_vip}')

recaudacion_total = 0.0
for concierto in lista_conciertos:
    recaudacion_total += concierto.calcular_recaudacion()
print(f'Recaudación total: {recaudacion_total} €')

precio_medio = recaudacion_total / total_entradas
print(f'Precio medio de las entradas: {precio_medio} €')

mas_vendido = lista_conciertos[0]
menos_vendido = lista_conciertos[0]
max_entradas = len(mas_vendido.entradas_vendidas)
min_entradas = len(menos_vendido.entradas_vendidas)
for concierto in lista_conciertos:
    vendidas = len(concierto.entradas_vendidas)
    if vendidas > max_entradas:
        max_entradas = vendidas
        mas_vendido = concierto
    if vendidas < min_entradas:
        min_entradas = vendidas
        menos_vendido = concierto
print(f'Concierto con más entradas vendidas: {mas_vendido} ({max_entradas})')
print(f'Concierto con menos entradas vendidas: {menos_vendido} ({min_entradas})')
