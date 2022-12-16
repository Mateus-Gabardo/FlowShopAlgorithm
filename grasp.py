import heuristicaBuscaLocal
import heuristicaBuscaLocalSolucaoParcial as BLS
import heuristicaConstrutiva
import heuristicaConstrutivaNEH as NEH
import instances

#####################################################
# Implementação do algoritmo GRASP
# Greedy Randomized Adaptative Search Procedure
#####################################################

def defineConstrucaoSemiGulosa(data, nb_jobs, nb_machines, alfa, algoritmo):
    if algoritmo == heuristicaConstrutiva:
        return heuristicaConstrutiva.construcaoSimples(data, nb_jobs, nb_machines, alfa)
    else:
        return NEH.heuristicaNEH(data, nb_jobs, nb_machines, alfa)

def defineBuscaLocal(data, nb_jobs, nb_machines, algoritmo, seq_current):
    if algoritmo == heuristicaBuscaLocal:
        return heuristicaBuscaLocal.buscaLocalSimples(data, nb_jobs, nb_machines, 1, seq_current)
    else:
        return BLS.buscaLocalSolucaoParcial(data, nb_jobs, nb_machines, seq_current)


def graspBase(data, nb_jobs, nb_machines, alfa, construcao_semi_gulosa, busca_local):
    seq_current, cmax_current = defineConstrucaoSemiGulosa(data, nb_jobs, nb_machines, alfa, construcao_semi_gulosa)
    seq_current, cmax_current = defineBuscaLocal(data, nb_jobs, nb_machines, busca_local, seq_current)
    best_seq = seq_current
    cmax_best = cmax_current

    qtd_iteracoes = 25
    qtd_iteracoesSemMelhora = 10
    while qtd_iteracoes > 0 and qtd_iteracoesSemMelhora > 0:
        seq_current, cmax_current = defineConstrucaoSemiGulosa(data, nb_jobs, nb_machines, alfa, construcao_semi_gulosa)
        seq_current, cmax_current = defineBuscaLocal(data, nb_jobs, nb_machines, busca_local, seq_current)
        if cmax_best > cmax_current:
            cmax_best = cmax_current
            best_seq = seq_current

            qtd_iteracoesSemMelhora = 10
        else:
           qtd_iteracoesSemMelhora-= -1

        qtd_iteracoes-= 1

    return best_seq, cmax_best
    
# 1 - combinando algoritmo Heuristica Construtiva Simples com a de Busca local simples
# 2 - Combinando algoritmo Heuristica Construtiva Simples com a de Busca local em solucao parcial
# 3 - Combinando algoritmo de NEH com Busca Local Simples
# 4 - Combinando algoritmo de NEH com a de Busca local em solucao parcial 
def defineEstrategiaGrasp(data, nb_jobs, nb_machines, alpha, estrategia):
    best_seq = None
    cmax_best = None
    if estrategia == 1:
        best_seq, cmax_best = graspBase(data, nb_jobs, nb_machines, alpha, heuristicaConstrutiva, heuristicaBuscaLocal)

    elif estrategia == 2:
        best_seq, cmax_best = graspBase(data, nb_jobs, nb_machines, alpha, heuristicaConstrutiva, BLS)
    
    elif estrategia == 3:
        best_seq, cmax_best = graspBase(data, nb_jobs, nb_machines, alpha, NEH, heuristicaBuscaLocal)

    else:
        best_seq, cmax_best = graspBase(data, nb_jobs, nb_machines, alpha, NEH, BLS)
        
    return best_seq, cmax_best

#(nbj, nbm, seed, obj, array) = instances.generate(2)
#print(defineEstrategiaGrasp(array, nbj, nbm, 20, 4))
        