import random
import commonFunction as util
import heuristicaBuscaLocal as buscaSimples
import math
import instances
import numpy

def buscaParcial(seq_current, data, nb_jobs, nb_machines):
    jobsRemoved = []
    best_seq = list(seq_current)
    ##k = 2 (solução por Dubois-Lacoste, Pagnozzi e Stützle (2017))
    for i in range(2):
        jobsRemoved.append(best_seq.pop(random.randint(0, len(best_seq))))
    best_seq, min_cmax = buscaSimples.escolheMelhorVizinho(best_seq, data, nb_jobs - (i + 1), nb_machines)
    aux_seq = best_seq
    for i in range(2):
        walk = jobsRemoved.pop(0)
        for j in range(0, len(aux_seq)):
            tmp_seq = buscaSimples.insertion(aux_seq, j, walk)
            cmax_tmp = util.makespan(tmp_seq, data, nb_machines)[nb_machines - 1][len(tmp_seq)]
            print(tmp_seq, cmax_tmp)
            if min_cmax > cmax_tmp:
                best_seq = tmp_seq
                min_cmax = cmax_tmp
    return best_seq

def aceitacao(seq_current, cmax_curent, seq_new, cmax_new, data):
    if (cmax_curent >= cmax_new):
        return seq_new, cmax_new
    elif random.randrange(0.0, 1.0) < funcaoTp(cmax_curent, cmax_new, data):
        return seq_new, cmax_new
    else:
        return seq_current, cmax_curent

def funcaoTp(cmax_curent, cmax_new, data):
    row, col = numpy.shape(data)
    total = 1
    for i in range(row):
        aux_sum = sum(int(data[i][j]) for j in range(col))
        total += aux_sum
    total /= (row * col * 10)
    total *= 0.7
    return math.pow(math.e, (cmax_curent - cmax_new)/total)

def buscaLocalSolucaoParcial(data, nb_jobs, nb_machines):
    seq_inicial, cmax_best = buscaSimples.buscaLocalSimples(data, nb_jobs, nb_machines, 2)
    seq_best = seq_inicial
    #estagnação (50 iterações ou 20 buscas sem melhoras)
    qtd_iteracoes = 50
    qtd_iteracoesSemMelhora = 10

    while qtd_iteracoes > 0 or qtd_iteracoesSemMelhora > 0:       
        seq_current = buscaParcial(seq_best, data, nb_jobs, nb_machines)
        seq_current, cmax_curent = buscaSimples.escolheMelhorVizinho(seq_current, data, nb_jobs, nb_machines)
        if cmax_curent < cmax_best:
            cmax_best = cmax_curent
            seq_best = seq_current
            qtd_iteracoesSemMelhora = 10
        ##VERIFICAR ISTO!
        elif random.randrange(0.0, 1.0) < funcaoTp(cmax_best, cmax_curent, data):
            aceitacao(seq_best, cmax_best, seq_current, cmax_curent, data)
            qtd_iteracoesSemMelhora -= 1
        qtd_iteracoes -= 1
    return seq_best, cmax_best


(nbj, nbm, seed, obj, array) = instances.generate(10)
print(buscaLocalSolucaoParcial(array, nbj, nbm))