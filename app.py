#  Arquivo principal do sistema que calcula área geométricas que virão de outros arquivos
import area_circulo as circulo

def calcular_area_retangulo(base, altura):
    """Calcula a área de um retângulo dado sua base e altura."""
    return base * altura

def calcular_area_circulo(area):
    resultado_area_circulo = circulo.calcular_area_circulo(area)  # Exemplo de uso da função do outro arquivo
    return resultado_area_circulo

def calcular_area_triangulo(base, altura):
    """Calcula a área de um triângulo dado sua base e altura."""
    return (base * altura) / 2

def main():
    raio = 5
    valor_area_circulo = calcular_area_circulo(raio)
    print(f"A área do círculo com raio {raio} é: {valor_area_circulo}")
    


main()

