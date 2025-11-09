"""Module pour vérifier si une chaîne est un palindrome."""

#### Fonction secondaire
ACCENTS = "ÀÁÂÃÄÅàáâãäåÈÉÊËèéêëÌÍÎÏìíîïÒÓÔÕÖØòóôõöøÙÚÛÜùúûüÝýÿÇç"
SANS_ACCENTS = "AAAAAAaaaaaaEEEEeeeeIIIIiiiiOOOOOOooooooUUUUuuuuYyyCc"
table = str.maketrans(ACCENTS, SANS_ACCENTS)


def ispalindrome(p):
    """Vérifie si la chaîne p est un palindrome."""
    # votre code ici
    p = p.translate(table)
    p = p.lower()
    p = ''.join(c for c in p if c.isalnum())
    print(p)
    return p == p[::-1]

#### Fonction principale


def main():
    """Fonction principale pour tester la fonction ispalindrome."""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
