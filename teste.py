import instances
import heuristicaConstrutiva as heu1
import heuristicaConstrutivaNEH as heu2
import heuristicaBuscaLocal as busca1
import heuristicaBuscaLocalSolucaoParcial as busca2
import grasp
from datetime import datetime

def fxheu1():
    file = open('teste.txt', 'w')
    delta = 95
    for i in range(10):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        best_seq, best_cmax = heu1.construcaoSimples(array, nbj, nbm, delta)
        text = str(f'heu1: instance: {i}, delta: {delta}, upperBound: {int(instances.generate(i)[3])}, value: {int(best_cmax)}')
        #file.write(f'{text}\n')
        print(f'{text}')
    file.close()

def fxheu2():
    file = open('teste.txt', 'w')
    delta = 10
    for i in range(10):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        best_seq, best_cmax = heu2.heuristicaNEH(array, nbj, nbm, delta)
        text = str(f'heu2: instance: {i}, delta: {delta}, upperBound: {int(instances.generate(i)[3])}, value: {int(best_cmax)}')
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

def fxgrasp(estrategia):
    file = open('teste.txt', 'w')
    for i in range(10):
        (nbj, nbm, seed, obj, array) = instances.generate(i)
        best_seq, best_cmax = grasp.defineEstrategiaGrasp(array, nbj, nbm, estrategia)
        text = str(f'grasp{estrategia} -- instance: {i}, upperBound: {int(instances.generate(i)[3])}, value: {int(best_cmax)}')
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
            (nbj, nbm, seed, obj, array) = instances.generate(i)
            time = 'Duration: {}'.format(datetime.now() - start_time)
            text = str(f'grasp{j+1}: instance: {i}, alpha: {alpha}, upperBound: {int(instances.generate(i)[3])}, avg: {mediaGrasp(array, nbj, nbm, alpha, j + 1, size)}, time: {time}')
            file.write(f'{text}\n')
            print(f'{text}')
    file.close()

med(10, 5)