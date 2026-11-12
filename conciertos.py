# Entrada general, es la clase base de las demás entradas
class Entrada:
    def __init__(self, concierto):
        self.concierto = concierto

    # Precio base del concierto
    def get_precio_total(self):
        return self.concierto.precio_base

    # Texto de la entrada general
    def __str__(self):
        return f'Entrada general para {self.concierto.artista} - {self.get_precio_total()} €'


# Entrada de grada, hereda de Entrada
class EntradaGrada(Entrada):
    def __init__(self, concierto, asiento):
        super().__init__(concierto)
        self.asiento = asiento

    # Precio base del concierto
    def get_precio_total(self):
        return self.concierto.precio_base

    # Texto de la entrada de grada
    def __str__(self):
        return f'Entrada de grada para {self.concierto.artista} - {self.get_precio_total()} €'


# Entrada de pista, hereda de Entrada
class EntradaPista(Entrada):
    def __init__(self, concierto, de_pie):
        super().__init__(concierto)
        self.de_pie = de_pie

    # Precio base más el 10%
    def get_precio_total(self):
        return self.concierto.precio_base + self.concierto.precio_base * 10 / 100

    # Texto de la entrada de pista
    def __str__(self):
        return f'Entrada de pista para {self.concierto.artista} - {self.get_precio_total()} €'


# Entrada VIP, hereda de Entrada
class EntradaVIP(Entrada):
    def __init__(self, concierto, incluye_consumicion):
        super().__init__(concierto)
        self.incluye_consumicion = incluye_consumicion

    # Precio base más el 20% si incluye consumición, o más el 15% si no
    def get_precio_total(self):
        if self.incluye_consumicion:
            return self.concierto.precio_base + self.concierto.precio_base * 20 / 100
        else:
            return self.concierto.precio_base + self.concierto.precio_base * 15 / 100

    # Texto de la entrada VIP
    def __str__(self):
        return f'Entrada VIP para {self.concierto.artista} - {self.get_precio_total()} €'


# Concierto con sus datos y la lista de entradas vendidas
class Concierto:
    def __init__(self, artista, ciudad, precio_base, aforo_maximo, activo=True):
        self.artista = artista
        self.ciudad = ciudad
        self.precio_base = precio_base
        self.aforo_maximo = aforo_maximo
        self.entradas_vendidas = []
        self.activo = activo

    # Suma el precio total de todas las entradas vendidas
    def calcular_recaudacion(self):
        if len(self.entradas_vendidas) == 0:
            return 0.0
        recaudacion = 0.0
        for entrada in self.entradas_vendidas:
            recaudacion += entrada.get_precio_total()
        return recaudacion

    # Precio medio de las entradas vendidas
    def calcular_precio_medio(self):
        if len(self.entradas_vendidas) == 0:
            return 0.0
        return self.calcular_recaudacion() / len(self.entradas_vendidas)

    # True si quedan entradas según el aforo máximo, False si no
    def entradas_disponibles(self):
        return len(self.entradas_vendidas) < self.aforo_maximo

    # Texto del concierto
    def __str__(self):
        return f'Concierto de {self.artista} en {self.ciudad}'


# Usuario que compra entradas y valora los conciertos
class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.entradas_compradas = []
        self.conciertos_asistidos = set()
        self.valoraciones = {}

    # Compra una entrada del tipo indicado ('grada', 'pista' o 'vip')
    def comprar_entrada(self, concierto, tipo_entrada):
        if not concierto.activo:
            raise Exception(f'El concierto de {concierto.artista} no está activo')

        if concierto in self.conciertos_asistidos:
            raise Exception(f'{self.nombre} ya ha asistido al concierto de {concierto.artista}')

        if not concierto.entradas_disponibles():
            raise Exception(f'No quedan entradas disponibles para el concierto de {concierto.artista}')

        if tipo_entrada.lower() == 'grada':
            entrada = EntradaGrada(concierto, '1A')
        elif tipo_entrada.lower() == 'pista':
            entrada = EntradaPista(concierto, True)
        elif tipo_entrada.lower() == 'vip':
            entrada = EntradaVIP(concierto, True)
        else:
            entrada = Entrada(concierto)

        concierto.entradas_vendidas.append(entrada)
        self.entradas_compradas.append(entrada)
        self.conciertos_asistidos.add(concierto)

    # Añade o cambia la valoración (de 0 a 10) de un concierto al que ha asistido
    def valorar(self, concierto, valoracion):
        if concierto not in self.conciertos_asistidos:
            raise Exception(f'{self.nombre} no ha asistido al concierto de {concierto.artista}')

        if valoracion < 0 or valoracion > 10:
            raise Exception('La valoración tiene que estar entre 0 y 10')

        self.valoraciones[concierto] = valoracion

    # Texto del usuario con los conciertos a los que ha asistido
    def __str__(self):
        return f'{self.nombre} (ha asistido a {len(self.conciertos_asistidos)})'
