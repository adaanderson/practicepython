
with open('nameslist.txt', 'r') as open_file:
    names = {}
       
    while True:
        line = open_file.readline()
        if not line:
            break
        x = line.replace('\n', '')
        print(line)
        
        if names.get(x) == None:
            names[x] = 1
        else:    
            names[x] += 1

print(names)   