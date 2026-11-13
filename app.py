#  Arquivo principal do sistema que calcula área geométricas que virão de outros arquivos
import area_circulo as circulo

def calcular_area_retangulo():
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area_retangulo = base * altura
    return area_retangulo

def calcular_area_circulo(area):
    resultado_area_circulo = circulo.calcular_area_circulo(area)  # Exemplo de uso da função do outro arquivo
    return resultado_area_circulo

def calcular_area_triangulo():
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area_triangulo = 0.5 * base * altura
    return area_triangulo

def main():
    raio = 5
    valor_area_circulo = calcular_area_circulo(raio)
    print(f"A área do círculo com raio {raio} é: {valor_area_circulo}")
    
    area_retangulo = calcular_area_retangulo()
    print(f"A área do retângulo é: {area_retangulo}")

    area_triangulo = calcular_area_triangulo()
    print(f"A área do triângulo é: {area_triangulo}")

main()

#Comentário: O código acima é o arquivo principal do sistema que calcula áreas geométricas. Ele importa a função de cálculo de área do círculo de outro arquivo chamado "area_circulo.py". As funções para calcular a área do retângulo e do triângulo são definidas dentro deste arquivo. A função main() coordena a execução do programa, chamando as funções de cálculo e exibindo os resultados.