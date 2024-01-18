def funkcija4():
    try:
        with open ("fails.txt", 'r', encoding="utf8") as f:
            cetri = f.read()
            return cetri 
    except FileNotFoundError:
        print("Datne nav atrasta")
        
def funkcija44():
    ievade1 = input("Ievadi faila nosaukumu: ")
    ievade2 = input("Ievadi faila formātu: ")

    kopa = f"{ievade1}.{ievade2}"

    cetri = funkcija4(kopa) 
    
    if cetri is not None:
        print("Fails: {cetri}")



if __name__ == "__main__":
    funkcija4()

if __name__ == "__main__":
    funkcija44()
        