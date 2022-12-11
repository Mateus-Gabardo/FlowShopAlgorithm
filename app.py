import instances
import sys

instance = int(sys.argv[1])

#nbj = número de jobs
#nbm = número de máquinas
#seed = seed utilizado da instância
#obj = objetivo a ser alcançado (melhor resultado)
#array = matriz de tempos
(nbj, 
    nbm, 
    seed, 
    obj, 
    array) = instances.generate(instance)