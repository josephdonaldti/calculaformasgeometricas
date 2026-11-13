#  Arquivo principal do sistema que calcula área geométricas que virão de outros arquivos
import area_circulo as circulo

def calcular_area_retangulo():
    largura = 5
    altura = 3
    area = largura * altura
    print(f"A área do retângulo é: {area}")

def calcular_area_circulo(area):
    resultado_area_circulo = circulo.calcular_area_circulo(area)  # Exemplo de uso da função do outro arquivo
    return resultado_area_circulo

def calcular_area_triangulo():
    base = 6
    altura = 4

    area = (base * altura) / 2
    print(f"A área do triângulo é: {area}")

def main():
    raio = 5
    valor_area_circulo = calcular_area_circulo(raio)
    print(f"A área do círculo com raio {raio} é: {valor_area_circulo}")
    


main()

