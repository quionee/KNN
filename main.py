import random
import math
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from collections import Counter


def lerArquivoIris(nomeArquivo):
    with open(nomeArquivo) as file:
        linhas = file.read().splitlines()
    return linhas


def calcularDistanciaEuclidiana(instanciaTeste, instanciasTreinamento):
    distanciasEuclidianas = []

    for i in range(len(instanciasTreinamento[0])):
        d1 = (float(instanciaTeste[0]) - float(instanciasTreinamento[0][i][0])) ** 2
        d2 = (float(instanciaTeste[1]) - float(instanciasTreinamento[0][i][1])) ** 2
        d3 = (float(instanciaTeste[2]) - float(instanciasTreinamento[0][i][2])) ** 2
        d4 = (float(instanciaTeste[3]) - float(instanciasTreinamento[0][i][3])) ** 2
        distancia = [math.sqrt(d1 + d2 + d3 + d4), "Iris-setosa"]
        distanciasEuclidianas.append(distancia)

    for i in range(len(instanciasTreinamento[1])):
        d1 = (float(instanciaTeste[0]) - float(instanciasTreinamento[1][i][0])) ** 2
        d2 = (float(instanciaTeste[1]) - float(instanciasTreinamento[1][i][1])) ** 2
        d3 = (float(instanciaTeste[2]) - float(instanciasTreinamento[1][i][2])) ** 2
        d4 = (float(instanciaTeste[3]) - float(instanciasTreinamento[1][i][3])) ** 2
        distancia = [math.sqrt(d1 + d2 + d3 + d4), "Iris-versicolor"]
        distanciasEuclidianas.append(distancia)

    for i in range(len(instanciasTreinamento[2])):
        d1 = (float(instanciaTeste[0]) - float(instanciasTreinamento[2][i][0])) ** 2
        d2 = (float(instanciaTeste[1]) - float(instanciasTreinamento[2][i][1])) ** 2
        d3 = (float(instanciaTeste[2]) - float(instanciasTreinamento[2][i][2])) ** 2
        d4 = (float(instanciaTeste[3]) - float(instanciasTreinamento[2][i][3])) ** 2
        distancia = [math.sqrt(d1 + d2 + d3 + d4), "Iris-virginica"]
        distanciasEuclidianas.append(distancia)

    distanciasEuclidianas.sort()

    return distanciasEuclidianas


def calcularDistanciaEuclidianaSpambase(instanciaTeste, instanciasTreinamento, qtdAtributos):
    distanciasEuclidianas = []

    for i in range(len(instanciasTreinamento)):
        somatorio = 0.0
        for j in range(qtdAtributos - 1):
            somatorio += ((float(instanciaTeste[j]) - float(instanciasTreinamento[i][j])) ** 2)
        distancia = [math.sqrt(somatorio), instanciasTreinamento[i][qtdAtributos - 1]]
        distanciasEuclidianas.append(distancia)

    distanciasEuclidianas.sort()

    return distanciasEuclidianas


def print_cm(cm, labels, hide_zeroes=False, hide_diagonal=False, hide_threshold=None):
    columnwidth = max([len(x) for x in labels] + [5])  # 5 is value length
    empty_cell = " " * columnwidth

    print("    " + empty_cell, end=" ")
    for label in labels:
        print("%{0}s".format(columnwidth) % label, end=" ")

    print()

    for i, label1 in enumerate(labels):
        print("    %{0}s".format(columnwidth) % label1, end=" ")
        for j in range(len(labels)):
            cell = "%{0}.1f".format(columnwidth) % cm[i, j]

            if hide_zeroes:
                cell = cell if float(cm[i, j]) != 0 else empty_cell
            if hide_diagonal:
                cell = cell if i != j else empty_cell
            if hide_threshold:
                cell = cell if cm[i, j] > hide_threshold else empty_cell

            print(cell, end=" ")

        print()


def organizarInstancias(dados):
    instancias = []

    instancias.append([])
    instancias.append([])
    instancias.append([])

    for instancia in dados:
        instancia = instancia.split()
        if (instancia[4] == "Iris-setosa"):
            instancias[0].append(instancia)
        elif (instancia[4] == "Iris-versicolor"):
            instancias[1].append(instancia)
        else:
            instancias[2].append(instancia)
    
    return instancias


def separarInstancias(instancias, qtdInstanciasTeste, qtdInstanciasTreinamento):
    instanciasTeste = []
    instanciasTreinamento = []

    instanciasTreinamento.append([])
    instanciasTreinamento.append([])
    instanciasTreinamento.append([])

    for i in range(qtdInstanciasTreinamento):
        instancia = random.choice(instancias[0])
        instanciasTreinamento[0].append(instancia)
        instancias[0].remove(instancia)

        instancia = random.choice(instancias[1])
        instanciasTreinamento[1].append(instancia)
        instancias[1].remove(instancia)

        instancia = random.choice(instancias[2])
        instanciasTreinamento[2].append(instancia)
        instancias[2].remove(instancia)

    for i in range(3):
        for j in range(qtdInstanciasTeste):
            instanciasTeste.append(instancias[i][j])
    
    return [instanciasTeste, instanciasTreinamento]


def knn(k, instanciasTeste, instanciasTreinamento):
    print("\n\n")

    for i in range(len(k)):
        distanciasEuclidianas = []
        dadosVerdadeiros = []
        dadosPreditos = []
        for j in range(len(instanciasTeste)):
            distanciasEuclidianas = calcularDistanciaEuclidiana(instanciasTeste[j],
                                                                instanciasTreinamento)

            dadosVerdadeiros.append(instanciasTeste[j][4])

            if (i == 1):
                melhoresDistancias = []
                for l in range(k[1]):
                    melhoresDistancias.append(distanciasEuclidianas[l][1])
                
                ocorrencias = Counter(melhoresDistancias)
                dadosPreditos.append(ocorrencias.most_common(1)[0][0])

            elif (i == 2):
                melhoresDistancias = []
                for l in range(k[2]):
                    melhoresDistancias.append(distanciasEuclidianas[l][1])
                
                ocorrencias = Counter(melhoresDistancias)
                dadosPreditos.append(ocorrencias.most_common(1)[0][0])

            elif (i == 3):
                melhoresDistancias = []
                for l in range(k[3]):
                    melhoresDistancias.append(distanciasEuclidianas[l][1])

                ocorrencias = Counter(melhoresDistancias)
                dadosPreditos.append(ocorrencias.most_common(1)[0][0])
            
            else:
                dadosPreditos.append(distanciasEuclidianas[0][1])

        print("---------------------------- Para k =", k[i], "---------------------------\n\n")
        cm = confusion_matrix(dadosVerdadeiros, dadosPreditos, labels=["Iris-setosa",
                                                                       "Iris-versicolor",
                                                                       "Iris-virginica"])
        labels = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]
        print_cm(cm, labels)
        print("\n\nAcurácia: ", accuracy_score(dadosVerdadeiros, dadosPreditos))
        print("\nRecall: ", recall_score(dadosVerdadeiros, dadosPreditos, average=None))
        print("\nPrecisão: ", precision_score(dadosVerdadeiros, dadosPreditos, average=None))
        print("\nF-score: ", f1_score(dadosVerdadeiros, dadosPreditos, average=None), "\n\n\n")


def knnSpambase(k, instanciasTeste, instanciasTreinamento, qtdAtributos):
    print("\n\n")

    for i in range(len(k)):
        distanciasEuclidianas = []
        dadosVerdadeiros = []
        dadosPreditos = []

        for j in range(len(instanciasTeste)):
            distanciasEuclidianas = calcularDistanciaEuclidianaSpambase(instanciasTeste[j],
                                                                        instanciasTreinamento,qtdAtributos)
            dadosVerdadeiros.append(instanciasTeste[j][qtdAtributos - 1])

            if (i == 1):
                melhoresDistancias = []
                for l in range(k[1]):
                    melhoresDistancias.append(distanciasEuclidianas[l][1])
                
                ocorrencias = Counter(melhoresDistancias)
                dadosPreditos.append(ocorrencias.most_common(1)[0][0])

            elif (i == 2):
                melhoresDistancias = []
                for l in range(k[2]):
                    melhoresDistancias.append(distanciasEuclidianas[l][1])
                
                ocorrencias = Counter(melhoresDistancias)
                dadosPreditos.append(ocorrencias.most_common(1)[0][0])

            elif (i == 3):
                melhoresDistancias = []
                for l in range(k[3]):
                    melhoresDistancias.append(distanciasEuclidianas[l][1])

                ocorrencias = Counter(melhoresDistancias)
                dadosPreditos.append(ocorrencias.most_common(1)[0][0])
            
            else:
                dadosPreditos.append(distanciasEuclidianas[0][1])

        print("---------------------------- Para k =", k[i], "---------------------------\n\n")
        cm = confusion_matrix(dadosVerdadeiros, dadosPreditos, labels=['0', '1'])
        labels = ['0', '1']
        print_cm(cm, labels)
        print("\n\nAcurácia: ", accuracy_score(dadosVerdadeiros, dadosPreditos))
        print("\nRecall: ", recall_score(dadosVerdadeiros, dadosPreditos, average=None))
        print("\nPrecisão: ", precision_score(dadosVerdadeiros, dadosPreditos, average=None))
        print("\nF-score: ", f1_score(dadosVerdadeiros, dadosPreditos, average=None), "\n\n\n")


def lerArquivoSpambase(nomeArquivo, porcentagemInstanciasTreinamento):
    with open(nomeArquivo) as arquivo:
        linhas = arquivo.read().splitlines()
    
    qtdLinhas = len(linhas)
    conjuntoIndices =  {x for x in range(qtdLinhas)}
    
    qtdTotalInstanciasTreinamento = int(qtdLinhas * porcentagemInstanciasTreinamento)
    qtdTotalInstanciasTeste = qtdLinhas - qtdTotalInstanciasTreinamento

    indicesTeste = set(random.sample(range(qtdLinhas), qtdTotalInstanciasTeste))
    indicesTreinamento = conjuntoIndices - indicesTeste

    instanciasTeste = []
    instanciasTreinamento = []

    for indice in indicesTeste:
        lista = linhas[indice].strip().split(',')
        instanciasTeste.append([])
        for i in range(len(lista) - 1):
            instanciasTeste[-1].append(float(lista[i]))
        instanciasTeste[-1].append(lista[-1])
    
    for indice in indicesTreinamento:
        lista = linhas[indice].strip().split(',')
        instanciasTreinamento.append([])
        for i in range(len(lista) - 1):
            instanciasTreinamento[-1].append(float(lista[i]))
        instanciasTreinamento[-1].append(lista[-1])

    return [instanciasTeste, instanciasTreinamento]


def baseDeDadosIris(porcentagemInstanciasTreinamento, k):
    dados = lerArquivoIris("iris.data")

    instancias = organizarInstancias(dados)

    qtdInstanciasTreinamento = int(porcentagemInstanciasTreinamento * len(instancias[0]))
    qtdInstanciasTeste = int(len(instancias[0]) - qtdInstanciasTreinamento)

    instanciasTeste, instanciasTreinamento = separarInstancias(instancias, qtdInstanciasTeste,
                                                               qtdInstanciasTreinamento)

    knn(k, instanciasTeste, instanciasTreinamento)


def baseDeDadosSpam(porcentagemInstanciasTreinamento, k):
    instanciasTeste, instanciasTreinamento = lerArquivoSpambase("spambase/spambase.data", 
                                                                porcentagemInstanciasTreinamento)

    knnSpambase(k, instanciasTeste, instanciasTreinamento, len(instanciasTeste[0]))


def main():
    porcentagemInstanciasTreinamento = 0.8
    k = [1, 3, 5, 7]

    print("\n\nBase de dados Iris")
    baseDeDadosIris(porcentagemInstanciasTreinamento, k)

    print("\n\nBase de dados Spam")
    baseDeDadosSpam(porcentagemInstanciasTreinamento, k)


if __name__ == "__main__":
    main()