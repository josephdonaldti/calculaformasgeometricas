# Arquivo principal do sistema que calcula áreas geométricas que virão de outros arquivos
import area_circulo as circulo
import area_retangulo as retangulo
import area_triangulo as triangulo

def calcular_area_retangulo(base, altura):
    return retangulo.calcular_area_retangulo(base, altura)

def calcular_area_circulo(raio):
    return circulo.calcular_area_circulo(raio)

def calcular_area_triangulo(base, altura):
    return triangulo.calcular_area_triangulo(base, altura)

def main():
    raio = 5
    base = 4
    altura = 3

    print(f"A área do círculo com raio {raio} é: {calcular_area_circulo(raio):.2f}")
    print(f"A área do retângulo {base}x{altura} é: {calcular_area_retangulo(base, altura)}")
    print(f"A área do triângulo (base {base}, altura {altura}) é: {calcular_area_triangulo(base, altura)}")

if __name__ == "__main__":
    main()