
#import random as r

from random import randint as rzut

gracz1 = []
gracz2 = []
gracz3 = []
gracz4 = []


lista_wynikow = {}
puste_wyniki = {"jedynki":0, "drójki":0, "trójki":0, "czwórki":0} #pusty słownik z wynikami


def rzut_kostkami (gracz="Gracz domyślny"):
    kubek = [0,0,0,0,0]
    reka = []
    for i in range (1,4):
        kosci_do_odlozenia = []
        #kubek_nowy = []
        #reka = []
        kubek = pojedynczy_rzut (kubek)

        print(gracz, "w rzucie", i, "wyrzucił:" , kubek)
        #co_odlozyc = input("Które kości zostawiasz? (jezeli różne, oddziel spacją): ")

        if i <= 2:
            kosci_do_odlozenia.extend([int(kosc) for kosc in input(f"{gracz} które kości zostawiasz? (jezeli różne, oddziel spacją, jeżeli nie zostawiasz nic podaj 0): ").split()])

            do_reki = jakie_kosci_zostaja(kubek, kosci_do_odlozenia)
            reka.extend(do_reki)
            reka.sort()
            print(f"  -->  {gracz} pozostawiasz kości: ", reka)

            if len(reka) == 5: break

            for kosc in do_reki:
                kubek.remove(kosc)

            print(f"  -->  {gracz} rzucasz kośćmi: ", kubek)
        else:
            reka.extend(kubek)
            reka.sort()
            print(f"{gracz} wyrzuciłeś w sumie", reka)

    return reka



def jakie_kosci_zostaja(kubek, kosci_do_odlozenia):
    reka = kubek.copy()
    kubek_nowy = list(set(kubek) - set(kosci_do_odlozenia))

    for kosc in kubek_nowy:
        for i in range (0, kubek.count(kosc)):
            reka.remove(kosc)

    return reka

def pojedynczy_rzut (kubek):
    for i in range(0,len(kubek)):
        kubek[i] = (rzut(1,6))
    return kubek

def wyswietl_wyniki(czyje="wszystkie"):
    if czyje == "wszystkie":
        for gracz in lista_wynikow:
            print(f"wyniki {gracz}:")
            for wyniki in lista_wynikow[gracz]:
                print (wyniki, ": ", lista_wynikow[gracz][wyniki])
    else:
        print(f"wyniki {czyje}:")
        for wyniki in lista_wynikow[czyje]:
                print (wyniki, ": ->", lista_wynikow[czyje][wyniki])

while True:
    gracze = [] #wyczyszczenie nazw graczy
    while True:
        try:
            ilu_graczy = int(input("podaj ulość graczy od 1 do 4: "))
            if ilu_graczy >=1 and ilu_graczy <= 4:
                break
        except:
            print("spróbój jeszcze raz --> ")

    for i in range (0,ilu_graczy):
        imie_gracza =  input(f"podaj imię gracza numer {i+1}: ").capitalize()
        gracze.append(imie_gracza)
        #lista_wynikow[imie_gracza] = puste_wyniki - tu miały zapisywac sie dane z wynikami graczy


    #wyswietl_wyniki(input("czyj ewyniki wyświetlić? ").capitalize())

    for gracz in gracze:
        lista_wynikow [gracz] = rzut_kostkami(gracz)
    #rzut_kostkami (gracz2)

    for gracz in gracze:
        print (gracz, "wyrzucił" , lista_wynikow[gracz])

    #print(lista_wynikow)


    #rzut_kostkami (gracz2)

    if input("grasz dalej: ? T/N").upper()== "N": break
