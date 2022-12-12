import instances
import heuristicaConstrutiva as heuConst
import heuristicaConstrutivaNEH as neh

def begin():
    instance = instances.getInstances()
    listModelo = getModelo()
    selModelo = 0
    for i in range(len(listModelo)):
        print(f'{i+1} - {listModelo[i]}')
    while True:
        try:
            selModelo = int(input('Selecione o modelo: ')) - 1
            if selModelo >= 0 or selModelo < int(len(listModelo) - 1):
                break
        except:
            print('Modelo incorreto, selecione novamente!')
    for i in range(len(instance)):
        text = instance[i].split('/')[2]
        text = text.split('.')[0]
        print(f'{i+1} - {text}')
    while True:
        try:
            selInstance = int(input('Selecione um número acima para selecionar a instância: ')) - 1
            selStrategy = int(input('Selecione um percentual de estratégia (0 para gulosa): '))
            if selInstance > 0 or selInstance <= int(len(instance)):
                #nbj = número de jobs
                #nbm = número de máquinas
                #seed = seed utilizado da instância
                #obj = objetivo a ser alcançado (melhor resultado)
                #array = matriz de tempos
                (nbj, nbm, seed, obj, array) = instances.generate(selInstance)
                if isinstance(selStrategy, int) and (selStrategy > 0 or selStrategy <= 100):
                    if selStrategy == 0:
                        heuristica_construtiva(array, nbj, nbm, obj, selModelo)
                    else:
                        heuristica_construtiva(array, nbj, nbm, obj, selModelo, selStrategy)
                break
        except:
            print('Valores informados inválidos. Informar novamente!')

def getModelo():
    list = ['Heurística do menor para o maior', 'Heurística NEH']
    return list


def heuristica_construtiva(data, nb_jobs, nb_machines, objetivo, modelo, estrategia = 0):
    while True:
        if modelo == 0:
            bestSeq, makespan = heuConst.construcaoSimples(data, nb_jobs, nb_machines, estrategia)
        elif modelo == 1:
            bestSeq, makespan = neh.heuristicaNEH(data, nb_jobs, nb_machines, estrategia)
        else:
            print('Modelo incorreto!')
            break
        print('Melhor sequência:')
        print(bestSeq)
        print('Objetivo:', objetivo, ', makespan:', makespan)
        break

begin()