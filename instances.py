import os

def getInstances():
    locate = './instances/'
    files = os.listdir(locate)
    list = []
    for i in range(len(files)):
        list.append(locate + files[i])
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
            if 'numberOfJobs' in line: nbj = int(extract_settings(line)[0])
            if 'numberOfMachines' in line: nbm = int(extract_settings(line)[0])
            if 'initialSeed' in line: seed = int(extract_settings(line)[0])
            if 'upperBound' in line: obj = float(extract_settings(line)[0])
            if 'line' in line: array.append(extract_array(line))
    file.close()
    return nbj, nbm, seed, obj, array

print(getInstances())