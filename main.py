"""Application console de gestion des tâches (Partie 1)."""

taches = []  


def afficher_menu():
    print("\n=== GESTION DES TÂCHES ===")
    print("1. Ajouter une tâche   2. Afficher   3. Rechercher   0. Quitter")


def ajouter_tache():
    titre = input("Titre de la tâche : ").strip()
    if titre == "":
        print("Erreur : le titre ne peut pas être vide.")
        return
    taches.append(titre)
    print("Tâche ajoutée avec succès.")


def afficher_taches():
    if len(taches) == 0:
        print("Aucune tâche pour le moment.")
        return
    for i in range(len(taches)):
        print(f"{i + 1}. {taches[i]}")
    print(f"Total : {len(taches)} tâche(s)")




def main():
    choix = ""
    while choix != "0":
        afficher_menu()
        choix = input("Votre choix : ").strip()
        if choix == "1":
            ajouter_tache()
        elif choix == "2":
            afficher_taches()
        elif choix == "3":
            rechercher_tache()
        elif choix == "0":
            print("Au revoir !")
        else:
            print("Option invalide, choisissez 1, 2, 3 ou 0.")


if __name__ == "__main__":
    main()
