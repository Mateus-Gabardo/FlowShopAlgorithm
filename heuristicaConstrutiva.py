import commonFunction
import random
import numpy
import math

#####################################################
# Heuristica construtiva
#####################################################


def avaliacao(percentEstrategy, componentes):
    if percentEstrategy == 0:
        return componentes[0]
    else:
        #Seleciona os x% melhores
        c_melhor = []
        percent =  math.ceil(len(componentes) * (percentEstrategy/100))
        for i in range(percent):
            c_melhor.append(componentes[i])
        return random.choice(c_melhor)

# Heuristica de construção simples Gulosa e Semi-gulosa
# Retorna a melhor sequencia encontrada, e o mankspan da matriz
def construcaoSimples(data, nb_jobs, nb_machines, estrategia = 0):
    #componentes - correspondem aos componentes iniciais
    # ja vem ordenados de acordo com a relação de tempo n*m
    seq_current = commonFunction.ordena(data, nb_jobs, nb_machines)
    best_seq = numpy.zeros(len(seq_current), dtype= int)
    for c in range(len(seq_current)):
        esc = avaliacao(estrategia, seq_current)
        best_seq[c] = esc;
        seq_current.remove(esc)
    return best_seq, commonFunction.makespan(best_seq, data, nb_machines)[nb_machines - 1][nb_jobs]