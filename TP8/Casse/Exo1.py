longueur_totale = 0
largeur_totale = 0
num_part = 0
aire = 0


def solu():
    global longueur_totale
    global largeur_totale
    global num_part
    global aire
    f = open("test01.in")
    largeur_totale = int(f.readline())
    num_part = int(f.readline())
    print("L" + str(largeur_totale) + "n" + str(num_part))


    for i in range (num_part) :
        l, h = f.readline().split()
        aire += int(l)*int(h)

    longueur_totale = aire/largeur_totale

    print(str(longueur_totale))
