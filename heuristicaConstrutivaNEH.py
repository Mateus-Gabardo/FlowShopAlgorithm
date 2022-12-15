import commonFunction as util
import numpy as np
import math
import random

#####################################################
# Heuristica constutiva NEH
# Heuristica construtiva simples baseado em Nawaz, Enscore e Ham
#####################################################


def insertion(sequence, index_position, value):
    new_seq = sequence[:]
    new_seq.insert(index_position, value)
    return new_seq

def ordenaMap(dict):
    keys = list(dict.keys())
    values = list(dict.values())
    sorted_value_index = np.argsort(keys)
    return {keys[i]: values[i] for i in sorted_value_index}

def avaliacao(percentEstrategy, componentes):
    if percentEstrategy == 0:
        return list(componentes.values())[0]
    else:
        #Seleciona os x% melhores
        c_melhor = []
        percent =  math.ceil(len(list(componentes.keys())) * (percentEstrategy/100))
        for i in range(percent):
            c_melhor.append(list(componentes.values())[i])
        return random.choice(c_melhor)

def heuristicaNEH(data, nb_jobs, nb_machines, estrategia = 0):
    """
    1. Para cada trabalho j, calcule o tempo total de processamento Pj nas m máquinas:
    2. Ordene de forma decrescente os trabalhos de acordo com Pj.
    """
    order_seq = util.ordena(data, nb_jobs, nb_machines, True)
    seq_current = [order_seq[0]]
    for i in range(1, nb_jobs):
        min_cmax = float("inf")
        aux = {}
        for j in range(0, i + 1):

            tmp_seq = insertion(seq_current, j, order_seq[i])
            cmax_tmp = util.makespan(tmp_seq, data, nb_machines)[nb_machines - 1][len(tmp_seq)]

            aux[cmax_tmp] = tmp_seq
            #print(tmp_seq, cmax_tmp)
            if min_cmax > cmax_tmp:
                best_seq = tmp_seq
                min_cmax = cmax_tmp
        if estrategia != 0:
           seq_current = avaliacao(estrategia, ordenaMap(aux))
        else:
            seq_current = best_seq
        #print()
        
    return seq_current, util.makespan(seq_current, data, nb_machines)[nb_machines - 1][nb_jobs]