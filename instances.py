def getInstances():
    file = open ("./instances.txt", 'r')
    list = file.read().splitlines()
    return list

def extract_settings(line):
    content = line.split('=')[-1]
    return content.split('=')

def extract_array(line):
    content = line.split('=')[-1]
    array = content.split(',')
    return array

def generate(instance):
    global nbj, nbm, seed, obj, array
    array = []
    instances = getInstances()
    file = open(instances[instance], 'r')
    for line in file.readlines():
        line = line.strip()
        if line != '' and line[0] != '#':
            if 'numberOfJobs' in line: nbj = extract_settings(line)
            if 'numberOfMachines' in line: nbm = extract_settings(line)
            if 'initialSeed' in line: seed = extract_settings(line)
            if 'upperBound' in line: obj = extract_settings(line)
            if 'line' in line: array.append(extract_array(line))
    file.close()
    return nbj, nbm, seed, obj, array