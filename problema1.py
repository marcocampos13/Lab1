import math

# Clase base para geometría
class Geometria:
    def area(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def formula(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

# Clase para Cuadrado
class Cuadrado(Geometria):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def formula(self):
        return "Área = lado²"

# Clase para Rectángulo
class Rectangulo(Geometria):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def formula(self):
        return "Área = base * altura"

# Clase para Triángulo
class Triangulo(Geometria):
    def __init__(self, lado1, lado2, lado3):
        self.lados = [lado1, lado2, lado3]

    def area(self):
        # Usar la fórmula de Herón
        s = sum(self.lados) / 2
        return math.sqrt(s * (s - self.lados[0]) * (s - self.lados[1]) * (s - self.lados[2]))

    def formula(self):
        return "Área = √s(s-a)(s-b)(s-c), donde s = (a+b+c)/2"

    def tipo_triangulo(self):
        if len(set(self.lados)) == 1:
            return "Equilátero"
        elif len(set(self.lados)) == 2:
            return "Isósceles"
        else:
            return "Escaleno"

# Ejemplo de uso
cuadrado = Cuadrado(4)
rectangulo = Rectangulo(4, 6)
triangulo = Triangulo(3, 4, 5)

# Imprimir áreas y fórmulas
print(f"Cuadrado: Área = {cuadrado.area()}, Fórmula: {cuadrado.formula()}")
print(f"Rectángulo: Área = {rectangulo.area()}, Fórmula: {rectangulo.formula()}")
print(f"Triángulo: Área = {triangulo.area()}, Fórmula: {triangulo.formula()}")
print(f"Tipo de triángulo: {triangulo.tipo_triangulo()}")
