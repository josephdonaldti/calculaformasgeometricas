#  Arquivo principal do sistema que calcula área geométricas que virão de outros arquivos
import area_circulo as circulo

def calcular_area_retangulo():
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))

def calcular_area_circulo(area):
    raio = float(input("Digite o raio do círculo: "))
    area = circulo.calcular_area_circulo(raio)
    return area

def calcular_area_triangulo():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = (base * altura) / 2
    return area

def main():
    raio = 5
    valor_area_circulo = calcular_area_circulo(raio)
    print(f"A área do círculo com raio {raio} é: {valor_area_circulo}")
    


main()

