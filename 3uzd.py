#Izveidot Python programmu, 
#kas nolasītu un izdrukātu trešās teksta faila rindas saturu. 

import csv

def funkcija3():
    try: 
        with open ("putns.txt", 'r', encoding='utf8') as f:
            tris = csv.reader(f)
        for rinda in tris:
            if len(rinda) > 2:
                print(rinda[2])
    except FileNotFoundError:
        print("Datne nav atrasta")

if __name__ == "__main__":
    funkcija3()