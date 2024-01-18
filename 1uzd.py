def funkcija():
    try:
       with open("teksts.txt",'r', encoding='utf8') as f:
           viens=f.readlines()
           print(viens)

    except FileNotFoundError:
        print("Datne nav atrasta!")


if __name__=="__main__":
    funkcija()