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

# Insere um elemento em uma dada posição do array gerando a perutação dos elementos
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
    aux_seq = list(seq_current)
    best_seq = []
    walk = aux_seq.pop(jobSorted)
    min_cmax = float("inf")
    for j in range(0, nb_jobs):
        tmp_seq = insertion(aux_seq, j, walk)
        cmax_tmp = util.makespan(tmp_seq, data, nb_machines)[nb_machines - 1][len(tmp_seq)]
        #print(tmp_seq, cmax_tmp)

        if min_cmax > cmax_tmp:
            best_seq = tmp_seq
            min_cmax = cmax_tmp
            if j > 0 and estrategia == 2:
                return best_seq, min_cmax

    return best_seq, min_cmax

def defineSolucaoInicial(data, nb_jobs, nb_machines, solucaoInicialDefinido = None):
    ramdom_seq = None
    if solucaoInicialDefinido is None:
        ramdom_seq = solucaoInicial(nb_jobs)
    else:
        ramdom_seq = solucaoInicialDefinido

    best_cmax = util.makespan(ramdom_seq, data, nb_machines)[nb_machines - 1][len(ramdom_seq)]
    return ramdom_seq, best_cmax


# Algoritmo de busca local simples.
# estrategia - define o tipo de retorno: 
#   1- retorna a melhor melhoria entre todos os vizinhos
#   2 -retorna o primeiro vizinho melhor
def buscaLocalSimples(data, nb_jobs, nb_machines, estrategia = 1, solucaoInicialDefinido = None):
    # Retorna uma solução inicial de maneira aletório que será permutada durante a busca local    
    best_seq, best_cmax = defineSolucaoInicial(data, nb_jobs, nb_machines, solucaoInicialDefinido)

    qtd_iteracoes = 50
    
    while int(qtd_iteracoes) > 0 :
        seq_current, min_cmax = escolheMelhorVizinho(best_seq, data, nb_jobs, nb_machines, estrategia)        
        if(min_cmax < best_cmax):
            best_cmax = min_cmax
            best_seq = seq_current
        qtd_iteracoes = qtd_iteracoes - 1

    return best_seq, best_cmax

#nbj, nbm, seed, obj, array) = instances.generate(10)
#print(buscaLocalSimples(array, nbj, nbm, obj))