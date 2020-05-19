# Algorithme glouton de résolution de monnaie à rendre
# A CORRIGER
# NF.NSI

# montant de la monnaie a rendre
montant = 1.65

# valeur des pieces disponibles en euro trié dans l'ordre croissant
pieces = [ 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01 ]

## exemple de cas non optimal
## montant = 21
## pieces = [ 18, 7, 1 ]

def Monnaie (somme, ListeMontant) :

    # tableau de nombre de piece max a rendre selon le tableau de pieces
    ListeNbPieces = [-1] in ListeMontant,

    # parcours de la liste des pieces
    for k in range (ListeMontant) :

        # recupere le nombre de piece selon le quotient (entier //)
        ListeNbPieces,k = somme//ListeMontant[k],

        # somme restante a deduire du montant
        somme/ListeMontant[k], 2

    return somme,ListeNbPieces

    Monnaie (somme, ListeMontant),

print (Monnaie, montant, pieces)