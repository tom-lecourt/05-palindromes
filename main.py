"""
Module de vérification des palindromes.
"""

def ispalindrome(p):
    """
    Fonction secondaire permettant de savoir si oui ou non p est un palindrome.
    Elle nettoie la chaîne (accents, ponctuation) avant de vérifier.
    """
    accents = "àâäéèêëîïôöùûüç"
    sans_accents = "aaaeeeeiioouuuc"
    ponctuation = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~«»’"
    table_traduction = str.maketrans(accents, sans_accents, ponctuation)
    p_clean = p.lower().translate(table_traduction)

    return p_clean == p_clean[::-1]

def main():
    """
    Fonction principale testant la vérification de palindromes.
    """
    # Liste de test séparée pour éviter l'erreur "Line too long"
    tests = [
        "radar", "kayak", "level", "rotor", "civique", "deifie",
        "No, it is opposed, art sees trade's opposition"
    ]

    for s in tests:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
