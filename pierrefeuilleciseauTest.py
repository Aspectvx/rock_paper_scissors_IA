import random
print("🎮 Bienvenue dans Pierre Feuille Ciseaux !")

choix = input("Pierre, feuille ou ciseaux ? ").lower()

while choix in ["pierre", "feuille", "ciseaux"]:
    choix_ia = random.choice(["pierre", "feuille", "ciseaux"])
    print("🤖 IA :", choix_ia)

    if choix == choix_ia:
        print("🤝 Égalité !")

    elif (
        (choix == "pierre" and choix_ia == "ciseaux") or
        (choix == "feuille" and choix_ia == "pierre") or
        (choix == "ciseaux" and choix_ia == "feuille")
    ):
        print("🏆 Tu gagnes !")

    else:
        print("💀 Tu perds !")
    choix = input("Pierre, feuille ou ciseaux ? ").lower() 