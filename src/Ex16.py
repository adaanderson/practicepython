import string
import random

def char_range(c1, c2):
    x = [chr(c) for c in range(ord(c1), ord(c2)+1)]
    return x 
        
symbols = list("!@#$%^&*()_+/?")

def main():
    #all = [string]
    
    all = char_range('A', 'Z') + char_range('a', 'z') + char_range('0', '9') + symbols
    password = ''.join(random.sample(all, k=9))
    #[all[e] for e in random.sample(range(0, len(all)), 9)]
    print(password)

if __name__ == "__main__":
    main()

