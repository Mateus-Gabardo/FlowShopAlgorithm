import commonFunction as util
#####################################################
# algorithm for NEH
# Heuristica construtiva simples baseado em Nawaz, Enscore e Ham
#####################################################


def insertion(sequence, index_position, value):
    new_seq = sequence[:]
    new_seq.insert(index_position, value)
    return new_seq



def heuristicaNEH(data, nb_jobs, nb_machines, estrategia = 0):
    """
    1. Para cada trabalho j, calcule o tempo total de processamento Pj nas m máquinas:
    2. Ordene de forma decrescente os trabalhos de acordo com Pj.
    """
    order_seq = util.ordena(data, nb_jobs, nb_machines, True)
    seq_current = [order_seq[0]]
    for i in range(1, nb_jobs):
        min_cmax = float("inf")
        for j in range(0, i + 1):
            tmp_seq = insertion(seq_current, j, order_seq[i])
            cmax_tmp = util.makespan(tmp_seq, data, nb_machines)[nb_machines - 1][len(tmp_seq)]
            print(tmp_seq, cmax_tmp)
            if min_cmax > cmax_tmp:
                best_seq = tmp_seq
                min_cmax = cmax_tmp
        seq_current = best_seq 
    return seq_current, util.makespan(seq_current, data, nb_machines)[nb_machines - 1][nb_jobs]