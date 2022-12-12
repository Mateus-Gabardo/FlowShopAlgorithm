import instances
import heuristicaConstrutiva as heuConst
import heuristicaConstrutivaNEH as neh

def begin():
    instance = instances.getInstances()
    list = []
    for i in range(len(instance)):
        text = instance[i].split('/')[2]
        text = text.split('.')[0]
        print(f'{i+1} - {text}')
    while True:
        try:
            selInstance = int(input('Selecione um número acima para selecionar a instância: '))
            selStrategy = int(input('Selecione um percentual de estratégia (0 para gulosa): '))
            if selInstance > 0 or selInstance <= int(len(instance)) + 1:
                selInstance = int(selInstance) - 1
                #nbj = número de jobs
                #nbm = número de máquinas
                #seed = seed utilizado da instância
                #obj = objetivo a ser alcançado (melhor resultado)
                #array = matriz de tempos
                (nbj, nbm, seed, obj, array) = instances.generate(selInstance)
                if isinstance(selStrategy, int) and (selStrategy > 0 or selStrategy <= 100):
                    if selStrategy == 0:
                        heuristica_construtiva(array, nbj, nbm, obj)
                    else:
                        heuristica_construtiva(array, nbj, nbm, obj, selStrategy)
                break
        except:
            print('Valores informados inválidos. Informar novamente!')

def heuristica_construtiva(data, nb_jobs, nb_machines, objetivo, estrategia = 0):
    #bestSeq, makespan = heuConst.construcaoSimples(data, nb_jobs, nb_machines, estrategia)
    bestSeq, makespan = neh.heuristicaNEH(data, nb_jobs, nb_machines, estrategia)
    print('Melhor sequência:')
    print(bestSeq)
    print('Objetivo:', objetivo, ', makespan:', makespan)

begin()