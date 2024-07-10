with open('happynumbers.txt', 'r') as open_file:
    line = open_file.readline()
    happy = []
    while line:
        x = line.replace('\n', '')
        happy.append(x)
        line = open_file.readline()

with open('primenumbers.txt', 'r') as open_file:
    line = open_file.readline()
    prime = []
    while line:
        y = line.replace('\n', '')
        prime.append(y)
        line = open_file.readline()

common = []
for element in happy:
    if element in prime:
        common.append(element) 
print(common)
