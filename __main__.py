
import random
def main():
    a = input("Adivina el numero.\nJugar?(y/n)\n").lower().strip()
    if a == "y":
        intentos = 0
        num_player = None
        num = random.randint(0, 17)
        print("Adivina en que numero estoy pensando.\n")
        while num != num_player:
            num_player = int(input(">>> "))
            if num_player == num:
                print("Has ganado!\nNumero de intentos [", intentos, "]")
            elif num_player > num:
                print("Te has pasado, menos.\n")
                intentos += 1
            elif num_player < num:
                print("Te has pasado, mas.\n")
                intentos += 1
    else:
        print("po mu bien.\n")
        exit()



if __name__ == '__main__':
    main()