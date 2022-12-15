#####################################################
# Implementação do algoritmo GRASP
# Greedy Randomized Adaptative Search Procedure
#####################################################

def graspBase(data, nb_jobs, nb_machines, construcao_semi_gulosa, busca_local):
    seq_current = construcao_semi_gulosa(data, nb_jobs, nb_machines, 20)
    best_seq = busca_local(data, nb_jobs, nb_machines)

    qtd_iteracoes = 50
    qtd_iteracoesSemMelhora = 10
    while qtd_iteracoes > 0 and qtd_iteracoesSemMelhora > 0:

        qtd_iteracoes-=- 1