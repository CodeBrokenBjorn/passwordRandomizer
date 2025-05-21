import random 

num = "123454534545"
textRandom = "Warhammer"
textlenght = 0
new_index = "fsdagf"
tempValue = []


    

def main():
    looptimes = 0
    while looptimes < 5:
        text = zip(textRandom.lower(), num)
        print(list(text))
        
        combo = ""
        
        for c, n in zip(textRandom.lower(), num):
            combo += c + n
    
        char_list = list(combo)
        
        shuffled = char_list.copy()
        random.shuffle(shuffled)
        
        print("Original", "".join(char_list), "\n", "Shuffle", "".join(shuffled))
        
        looptimes += 1     
    
if "__main__" == __name__:
    main()
    
