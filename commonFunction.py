import numpy


# calculate the c_ij table.
def makespan(my_seq, p_ij, nbm):
    c_ij = numpy.zeros((nbm, len(my_seq) + 1))

    for j in range(1, len(my_seq) + 1):
        c_ij[0][j] = c_ij[0][j - 1] + float(p_ij[0][my_seq[j - 1]])

    for i in range(1, nbm):
        for j in range(1, len(my_seq) + 1):
            c_ij[i][j] = max(c_ij[i - 1][j], c_ij[i][j - 1]) + float(p_ij[i][my_seq[j - 1]])
    return c_ij

def sum_processing_time(index_job, data, nb_machines):
    sum_p = 0
    for i in range(nb_machines):
        sum_p += int(data[i][index_job])
    return sum_p


#data - matriz de mXn de máquinas por Jobs
# Retorna os elementos de jobs ordenados pela tempo de processamento n*m
def ordena(data, nb_jobs, nb_machines, reverse = False):
    components = []
    for j in range(nb_jobs):
        components.append(j)
    return sorted(components, key=lambda x: sum_processing_time(x, data, nb_machines), reverse= reverse)
            
