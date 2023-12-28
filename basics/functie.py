import math

# Definieer een functie genaamd 'bereken_oppervlakte_cirkel'


def bereken_oppervlakte_cirkel(r):
    """
    Deze functie berekent de oppervlakte van een cirkel gegeven de straal (r).
    """
    oppervlakte = math.pi * r**2
    return oppervlakte


# Vraag de gebruiker om de straal van de cirkel in te voeren
straal = float(input("Voer de straal van de cirkel in: "))

# Roep de functie aan om de oppervlakte te berekenen
oppervlakte_cirkel = bereken_oppervlakte_cirkel(straal)

# Geef het resultaat weer
print(
    f"De oppervlakte van de cirkel met straal {straal} is {oppervlakte_cirkel:.2f}.")
