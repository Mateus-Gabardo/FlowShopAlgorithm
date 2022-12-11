import commonFunction
import random
import numpy

#####################################################
# Heuristica construtiva
#####################################################

def sum_processing_time(index_job, data, nb_machines):
    sum_p = 0
    for i in range(nb_machines):
        sum_p += int(data[i][index_job])
    return sum_p

#data - matriz de mXn de máquinas por Jobs
# Retorna os elementos de jobs ordenados pela tempo de processamento n*m
def ordena(data, nb_jobs, nb_machines):
    components = []
    for j in range(nb_jobs):
        components.append(j)
    return sorted(components, key=lambda x: sum_processing_time(x, data, nb_machines))

def avaliacao(percentEstrategy, componentes):
    if percentEstrategy == 0:
        return componentes[0]
    else:
        #Seleciona os x% melhores
        c_melhor = []
        for i in range(int(componentes.count * percentEstrategy)):
            c_melhor.append(i)
        return random.choice(c_melhor)

# Heuristica de construção simples Gulosa e Semi-gulosa
# Retorna a melhor sequencia encontrada, e o mankspan da matriz
def construcaoSimples(data, nb_jobs, nb_machines, estrategia = 0):
    #componentes - correspondem aos componentes iniciais
    # ja vem ordenados de acordo com a relação de tempo n*m
    seq_current = ordena(data, nb_jobs, nb_machines)
    best_seq = numpy.zeros(len(seq_current), dtype= int)
    for c in range(len(seq_current)):
        esc = avaliacao(estrategia, seq_current)
        best_seq[c] = esc;
        seq_current.remove(esc)
    return best_seq, commonFunction.makespan(best_seq, data, nb_machines)[nb_machines - 1][nb_jobs]