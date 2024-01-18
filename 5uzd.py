def funkcija5():
    try:
        with open ("lietotajs.txt", 'r', encoding='utf8') as f:
            pieci = f.readlines()
            akk=int(input("Ievadi vārdu: "))
            if akk == "Evelīna":
                print("veiksmīga darbība!")
            else:
                print("kļūda!")


    except FileNotFoundError:
        print("datne nav atrasta")

if __name__ == "__main__":
    funkcija5()