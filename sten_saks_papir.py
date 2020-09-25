from random import randint #importerer biblioteket random - random intgerer

#Variabler deklareres
Sten = "Sten"
Saks = "Saks"
Papir = "Papir"

#Array "valgt" - som indeholder de tre variabler, sten, saks, papir.
valgt = ["sten", "saks", "papir"]

#Starter programmet igen når der indtastes en ny mulighed, kaldes i bunden af koden.
def main():

    # Få computeren til at vælge en random variabel fra array valgt.
    # (0,2) betyder det samme som at der er tre valgmuligheder 0, 1, 2.
    # randint tager to parametre, start og slut i arrayet.

    computer = valgt[randint(0,2)]

    # Brugerens valg
    print("Velkommen til Sten, saks, papir \n")
    # Omskriver svaret til små bogstaver, så det er lettere at sammenligne med computerens valg.
    brugerensValg = input("Dit valg er: ").lower()

    # Computerens valg
    print("Computerens valg er: " + computer)

    # Kan optimeres til færre steps
    if brugerensValg == computer:
        print("Uafgjort")
    elif brugerensValg == "sten" and computer == "papir":
        print("Desværre, du tabte!")
    elif brugerensValg == "sten" and computer == "saks":
        print("Tillykke, du vandt!")
    elif brugerensValg == "papir" and computer == "sten":
        print("Tillykke, du vandt!")
    elif brugerensValg == "papir" and computer == "saks":
        print("Desværre, du tabte!")
    elif brugerensValg == "saks" and computer == "sten":
        print("Desværre, du tabte!")
    elif brugerensValg == "saks" and computer == "papir":
        print("Tillykke, du vandt!")

    main()

main()

# https://www.youtube.com/watch?v=5wfxO_juzYM&ab_channel=TutorialSpot