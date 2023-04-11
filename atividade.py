def ler_valores():
    """
    Função para ler os valores de tempo e velocidade média da viagem.
    Retorna o tempo e a velocidade média informados pelo usuário.
    """
    tempo = float(input("Informe o tempo gasto na viagem (em horas): "))
    velocidade = float(input("Informe a velocidade média durante a viagem (em Km/h): "))
    return tempo, velocidade


def calcular_distancia(tempo, velocidade):
    """
    Função para calcular a distância percorrida na viagem.
    Recebe como parâmetro o tempo e a velocidade média informados pelo usuário.
    Retorna a distância percorrida.
    """
    distancia = tempo * velocidade
    return distancia


def calcular_litros(distancia):
    """
    Função para calcular a quantidade de litros de combustível utilizada na viagem.
    Recebe como parâmetro a distância percorrida.
    Retorna a quantidade de litros utilizada.
    """
    litros_usados = distancia / 12
    return litros_usados


def apresentar_resultado(tempo, velocidade, distancia, litros_usados):
    """
    Função para apresentar os resultados da viagem.
    Recebe como parâmetro os valores de tempo, velocidade média, distância e litros utilizados.
    Imprime na tela os resultados formatados.
    """
    print("Velocidade média: {} Km/h".format(velocidade))
    print("Tempo gasto na viagem: {} horas".format(tempo))
    print("Distância percorrida: {} Km".format(distancia))
    print("Quantidade de litros utilizada: {} litros".format(litros_usados))


# Função principal
def main():
    tempo, velocidade = ler_valores()
    distancia = calcular_distancia(tempo, velocidade)
    litros_usados = calcular_litros(distancia)
    apresentar_resultado(tempo, velocidade, distancia, litros_usados)


# Chamada da função principal
if __name__ == "__main__":
    main()