import random

def jouer():
    nombre_secret = random.randint(1, 100)
    print("Bienvenue dans le jeu de devinettes !")
    print("J'ai choisi un nombre entre 1 et 100. À toi de deviner !")

    essais = 0
    limite_essais = 10
    tandis_que = True

    while tandis_que and essais < limite_essais:
        try:
            proposition = int(input("Entre ton nombre : "))
            essais += 1

            if proposition < nombre_secret:
                print("C'est plus grand !")
            elif proposition > nombre_secret:
                print("C'est plus petit !")
            else:
                print(f"Bravo ! Tu as trouvé le nombre {nombre_secret} en {essais} essais.")
                tandis_que = False
        except ValueError:
            print("Merci d'entrer un nombre valide.")

    if essais >= limite_essais:
        print(f"Désolé, tu as dépassé la limite de {limite_essais} essais. Le nombre était {nombre_secret}.")

    print("Fin du jeu. Merci d'avoir joué !")

def main():
    rejouer = True
    while rejouer:
        jouer()
        reponse = input("Veux-tu rejouer ? (oui/non) : ").strip().lower()
        if reponse != 'oui':
            rejouer = False

if __name__ == "__main__":
    main()