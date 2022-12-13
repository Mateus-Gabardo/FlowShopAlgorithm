import random
import commonFunction as util
import instances

# Retorna a solução inicial de maneira aleatória
def solucaoInicial(nb_jobs):
    components = []
    for j in range(nb_jobs):
        components.append(j)
    return random.sample(components, len(components))

# Retorna o número de possibilidades de permutações.
def calculaFatorial(nb_jobs):
    result = 0
    for i in range(nb_jobs):
        result *= i
    return result

def insertion(sequence, index_position, value):
    new_seq = sequence[:]
    new_seq.insert(index_position, value)
    return new_seq

# Define a escolha de uma nova melhor solução a partir de vizinho gerados da solução inicial
# Conseguidos através de permutação de um elemento aleatório.
# estrategia - define o tipo de retorno: 
#   1- retorna a melhor melhoria entre todos os vizinhos
#   2 -retorna o primeiro vizinho melhor
def escolheMelhorVizinho(seq_current, data, nb_jobs, nb_machines, estrategia = 1):
    jobSorted = random.randrange(0, nb_jobs)
    best_seq = []
    walk = seq_current.pop(jobSorted)
    min_cmax = float("inf")
    for j in range(0, nb_jobs):
        tmp_seq = insertion(seq_current, j, walk)
        cmax_tmp = util.makespan(tmp_seq, data, nb_machines)[nb_machines - 1][len(tmp_seq)]
        print(tmp_seq, cmax_tmp)

        if min_cmax > cmax_tmp:
            best_seq = tmp_seq
            min_cmax = cmax_tmp
            if j > 0 and estrategia == 2:
                return best_seq

    return best_seq, min_cmax

def buscaLocalSimples(data, nb_jobs, nb_machines, estrategia = 0):
    # Retorna uma solução inicial de maneira aletório que será permutada durante a busca local
    ramdom_seq = solucaoInicial(nb_jobs)
    best_seq = ramdom_seq
    best_cmax = util.makespan(best_seq, data, nb_machines)[nb_machines - 1][len(best_seq)]

    qtd_iteracoes = calculaFatorial(nb_jobs)
    
    while int(qtd_iteracoes) > 0 :
        seq_current, min_cmax = escolheMelhorVizinho(best_seq, data, nb_jobs, nb_machines)        
        if(min_cmax < best_cmax):
            best_cmax = min_cmax
            best_seq = seq_current
        qtd_iteracoes = qtd_iteracoes - 1

    return best_seq, best_cmax

#(nbj, nbm, seed, obj, array) = instances.generate(10)
#print(buscaLocalSimples(array, nbj, nbm, obj))