import instances
import sys
import heuristicaConstrutiva as heuConst


def heuristica_construtiva(data, nb_jobs, nb_machines, objetivo, estrategia = 0):
    bestSeq, makespan = heuConst.construcaoSimples(data, nb_jobs, nb_machines, estrategia)
    print('Melhor sequência:')
    print(bestSeq)
    print('Objetivo: ', objetivo, 'makespan: ', makespan)


instance = int(sys.argv[1])

#nbj = número de jobs
#nbm = número de máquinas
#seed = seed utilizado da instância
#obj = objetivo a ser alcançado (melhor resultado)
#array = matriz de tempos
(nbj, nbm, seed, obj, array) = instances.generate(instance)
heuristica_construtiva(array, nbj, nbm, obj, 20)