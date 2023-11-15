# Atelier 2 : Les Fichiers

# 1. Ecrire un script fichie_ADN.py, qui ouvre et lit le contenu du fichier ADN.txt.
# Le fichier ADN.txt contient la chaine ci-dessous :
# A T C G G C T T A G A C G A T G A A G C C G T C C C G G A A A
def lire_fichier_ADN(nom_fichier):
    with open(nom_fichier, 'r') as fichier:
        contenu = fichier.read()
    return contenu
# 2. Ajouter la fonction calcule_taille_ADN qui calcule la longueur de la chaine
# ADN.
def calcule_taille_ADN(adn):
    return len(adn.split())
# 3. Ajouter la fonction nbr_A qui calcule le nombre des « A » dans le fichier
# ADN.txt.
def nbr_A(adn):
    return adn.count('A')
# 4. Ajouter la fonction nbr_C qui calcule le nombre des « C » dans le fichier
# ADN.txt.
def nbr_C(adn):
    return adn.count('C')
# 5. Ré-ouvrir le fichier ADN.txt en mode écriture et ajouter la fonction
# ADN_2_ARN qui génère l’ARN depuis l’ADN (en changeant le T par le U).
# - La nouvelle chaine ARN devra être en dessous de la chaine ADN.
def ADN_2_ARN(adn):
    arn = adn.replace('T', 'U')
    return arn

# Ouvrir et lire le contenu du fichier ADN.txt
nom_fichier = "ADN.txt"
contenu_ADN = lire_fichier_ADN(nom_fichier)
print(f"le contenu du fichier ADN.txt est {contenu_ADN}")

# Calculer la taille de la chaine ADN
taille_ADN = calcule_taille_ADN(contenu_ADN)
print(f"Taille de la chaine ADN : {taille_ADN} bases")

# Calculer le nombre de 'A' dans la chaine ADN
nombre_A = nbr_A(contenu_ADN)
print(f"Nombre de bases 'A' dans la chaine ADN : {nombre_A}")

# Calculer le nombre de 'C' dans la chaine ADN
nombre_C = nbr_C(contenu_ADN)
print(f"Nombre de bases 'C' dans la chaine ADN : {nombre_C}")

# Ré-ouvrir le fichier ADN.txt en mode écriture et ajouter la fonction ADN_2_ARN
with open(nom_fichier, 'a') as fichier:
    # Ajouter la chaine ARN après la chaine ADN
    arn = ADN_2_ARN(contenu_ADN)
    fichier.write("\n" + arn)

print("Conversion ADN vers ARN effectuée avec succès.")



