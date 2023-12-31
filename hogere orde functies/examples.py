def verdubbel(x):
    return x * 2


def drievoudig(x):
    return x * 3


def kwadraat(x):
    return x ** 2


def toepas_op_lijst(lijst, functie):
    """
    Pas de opgegeven functie toe op elk element van de lijst en retourneer de nieuwe lijst.
    """
    resultaat = []
    for element in lijst:
        resultaat.append(functie(element))
    return resultaat


if __name__ == "__main__":
    getallen = [1, 2, 3, 4, 5]

    # Gebruik van hogere-ordefunctie toepas_op_lijst
    verdubbelde_getallen = toepas_op_lijst(getallen, verdubbel)
    print("Verdubbelde getallen:", verdubbelde_getallen)

    drievoudige_getallen = toepas_op_lijst(getallen, drievoudig)
    print("Drievoudige getallen:", drievoudige_getallen)

    gekwadrateerde_getallen = toepas_op_lijst(getallen, kwadraat)
    print("Gekwadrateerde getallen:", gekwadrateerde_getallen)
