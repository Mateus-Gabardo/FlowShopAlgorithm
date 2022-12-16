import instances
import heuristicaConstrutiva as heu1
import heuristicaConstrutivaNEH as heu2
import heuristicaBuscaLocal as busca1
import heuristicaBuscaLocalSolucaoParcial as busca2
import grasp
from datetime import datetime

def fxheu1(alpha):
    file = open('teste.txt', 'w')
    for i in range(10):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        best_seq, best_cmax = heu1.construcaoSimples(array, nbj, nbm, alpha)
        text = str(f'heu1: instance: {i}, alpha: {alpha}, upperBound: {int(instances.generate(i)[3])}, value: {int(best_cmax)}')
        #file.write(f'{text}\n')
        print(f'{text}')
    file.close()

def fxheu2(alpha):
    file = open('teste.txt', 'w')
    for i in range(10):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        best_seq, best_cmax = heu2.heuristicaNEH(array, nbj, nbm, alpha)
        text = str(f'heu2: instance: {i}, alpha: {alpha}, upperBound: {int(instances.generate(i)[3])}, value: {int(best_cmax)}')
        #file.write(f'{text}\n')
        print(f'{text}')
    file.close()

def fxbusca1():
    file = open('teste.txt', 'w')
    for i in range(10):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        best_seq, best_cmax = busca1.buscaLocalSimples(array, nbj, nbm)
        text = str(f'busca1: instance: {i}, upperBound: {int(instances.generate(i)[3])}, value: {int(best_cmax)}')
        #file.write(f'{text}\n')
        print(f'{text}')
    file.close()

def fxbusca2():
    file = open('teste.txt', 'w')
    for i in range(10):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        best_seq, best_cmax = busca2.buscaLocalSolucaoParcial(array, nbj, nbm)
        text = str(f'busca2: instance: {i}, upperBound: {int(instances.generate(i)[3])}, value: {int(best_cmax)}')
        #file.write(f'{text}\n')
        print(f'{text}')
    file.close()
    return best_seq

def fxgrasp(alpha, estrategia):
    file = open('teste.txt', 'w')
    for i in range(10):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        best_seq, best_cmax = grasp.defineEstrategiaGrasp(array, nbj, nbm, alpha, estrategia)
        text = str(f'grasp{estrategia}: instance: {i}, alpha: {alpha}, upperBound: {int(instances.generate(i)[3])}, value: {int(best_cmax)}')
        #file.write(f'{text}\n')
        print(f'{text}')
    file.close()

def mediaHeu1(array, nbj, nbm, alpha, size):
    total = 0
    for i in range(size):
        best_seq, best_cmax = heu1.construcaoSimples(array, nbj, nbm, alpha)
        total += best_cmax
    return int(total / size)

def mediaHeu2(array, nbj, nbm, alpha, size):
    total = 0
    for i in range(size):
        best_seq, best_cmax = heu2.heuristicaNEH(array, nbj, nbm, alpha)
        total += best_cmax
    return int(total / size)

def mediaBusca1(array, nbj, nbm, size):
    total = 0
    for i in range(size):
        best_seq, best_cmax = busca1.buscaLocalSimples(array, nbj, nbm)
        total += best_cmax
    return int(total / size)

def mediaBusca2(array, nbj, nbm, size):
    total = 0
    for i in range(size):
        best_seq, best_cmax = busca2.buscaLocalSolucaoParcial(array, nbj, nbm)
        total += best_cmax
    return int(total / size)

def mediaGrasp(array, nbj, nbm, alpha, estrategia, size):
    total = 0
    for i in range(size):
        best_seq, best_cmax = grasp.defineEstrategiaGrasp(array, nbj, nbm, alpha, estrategia)
        total += best_cmax
    return int(total / size)

def med(instance, size):
    start_time = datetime.now()
    file = open('teste.txt', 'w')
    for i in range(instance):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        alpha = 95
        time = 'Duration: {}'.format(datetime.now() - start_time)
        text = str(f'heu1: instance: {i}, alpha: {alpha}, upperBound: {int(instances.generate(i)[3])}, avg: {mediaHeu1(array, nbj, nbm, alpha, size)}, time: {time}')
        file.write(f'{text}\n')
        print(f'{text}')
    for i in range(instance):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        alpha = 10
        time = 'Duration: {}'.format(datetime.now() - start_time)
        text = str(f'heu2: instance: {i}, alpha: {alpha}, upperBound: {int(instances.generate(i)[3])}, avg: {mediaHeu2(array, nbj, nbm, alpha, size)}, time: {time}')
        file.write(f'{text}\n')
        print(f'{text}')
    for i in range(instance):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        time = 'Duration: {}'.format(datetime.now() - start_time)
        text = str(f'busca1: instance: {i}, alpha: -, upperBound: {int(instances.generate(i)[3])}, avg: {mediaBusca1(array, nbj, nbm, size)}, time: {time}')
        file.write(f'{text}\n')
        print(f'{text}')
    for i in range(instance):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        time = 'Duration: {}'.format(datetime.now() - start_time)
        text = str(f'busca2: instance: {i}, alpha: -, upperBound: {int(instances.generate(i)[3])}, avg: {mediaBusca2(array, nbj, nbm, size)}, time: {time}')
        file.write(f'{text}\n')
        print(f'{text}')
    for j in range(4):
        for i in range(instance):
            if j <= 1:
                alpha = 95
            else:
                alpha = 10
            (nbj, nbm, seed, obj, array) = instances.generate(i)
            time = 'Duration: {}'.format(datetime.now() - start_time)
            text = str(f'grasp{j+1}: instance: {i}, alpha: {alpha}, upperBound: {int(instances.generate(i)[3])}, avg: {mediaGrasp(array, nbj, nbm, alpha, j + 1, size)}, time: {time}')
            file.write(f'{text}\n')
            print(f'{text}')
    file.close()

#Executa todas as instâncias e salva os resultados no arquivo teste.txt.
#Como parâmetros, informar a quantidade de instâncias a serem processadas,
#e quantas vezes o código será repetido para obter a média de resultados.
#med(10, 5)

#Executa a heurística 1. O parâmetro é: alfa guloso
fxheu1(50)

#Executa a heurística 2. O parâmetro é: alfa guloso
fxheu2(50)

#Executa a busca local 1.
fxbusca1()

#Executa a busca local 2.
fxbusca2()

#Executa o grasp. Os parâmetros são: alfa guloso, modelo do grasp.
#Os modelos do grasp são: 
#1: heurística 1 com busca local 1
#2: heurística 1 com busca local 2
#3: heurística 2 com busca local 1
#4: heurística 2 com busca local 2
fxgrasp(10, 1)