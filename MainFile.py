def login(utilisateur, mot_de_passe):
    return utilisateur == "admin" and mot_de_passe == "1234"

def main():
    print("Bienvenue ! Veuillez vous connecter.")
    if login("admin", "1234"):
        print("Connexion réussie.")
    deconnexion()
    print("Ligne à annuler")
        
        
def deconnexion():
    print("Vous êtes déconnecté.")

if __name__ == "__main__":
    main()