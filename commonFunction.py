
#Retorna as intancias do problema
def instances():
    return '';

def read_from_file(arquivo):
    with open(arquivo, "r") as fic:
        my_nbm = int(fic.readline())
        my_nbj = int(fic.readline())
        my_p_ij = None
        for i in range(my_nbm):
            p_i = fic.readline().split()
            for j in range(my_nbj):
                my_p_ij[i][j] = int(p_i[j])
    return my_nbm, my_nbj, my_p_ij