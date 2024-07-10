def convert(a):
    newstring = a.split()
    finalstring = " ".join(newstring[-1::-1])
    return finalstring

string = input("Give me a string with multiple words: ")
print(convert(string))