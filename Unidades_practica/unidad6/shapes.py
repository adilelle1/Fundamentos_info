class Esfera:

    def __init__(self, radio):
        self.nombre = "Esfera"
        self.radio = radio

    def get_nombre(self):
        return f"El nombre de la figura es: {self.nombre}"

    def get_radio(self):
        return f"El radio de la figura es: {self.radio}"

    def print_properties(self):
        return f"{self.nombre} con propiedades radio: {self.radio}"


class Cubo:

    def __init__(self, lado):
        self.nombre = "Cubo"
        self.lado = lado

    def get_nombre(self):
        return f"El nombre de la figura es: {self.nombre}"

    def get_lado(self):
        return f"El lado de la figura es: {self.lado}"

    def shape_preview(self):
        print(f'\t{"[]"*self.lado}')
        print('\t{:10}'.format('[]') + '[]')
        print('\t{:10}'.format('[]') + '[]')
        print('\t[][][][][][]')

    def print_properties(self):
        return f"{self.nombre} con propiedades lado: {self.lado}"


class PrismaRectangular:

    def __init__(self, base, altura, profundidad):
        self.nombre = "Prisma Rectangular"
        self.base = base
        self.altura = altura
        self.profundidad = profundidad

    def get_nombre(self):
        return f"El nombre de la figura es: {self.nombre}"

    def get_dimesiones(self):
        return f"El area de la figura es: {[self.base, self.altura, self.profundidad]}"

    def shape_preview(self):
        print('\t[][][][][][][][][]')
        print('\t{:16}'.format('[]') + '[]')
        print('\t{:16}'.format('[]') + '[]')
        print('\t[][][][][][][][][]')

    def print_properties(self):
        return f"{self.nombre} con propiedades: {[self.base, self.altura, self.profundidad]}"
