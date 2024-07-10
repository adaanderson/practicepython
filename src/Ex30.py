from random import sample

with open('sowpods.txt', 'r') as open_file:
    names = set()
       
    while True:
        line = open_file.readline()
        if not line:
            break
        x = line.replace('\n', '')
        names.add(x)
        
print(sample(names,1))