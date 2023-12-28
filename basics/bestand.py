# Definieer de naam van het tekstbestand
bestandsnaam = 'mijn_bestand.txt'

# Open het bestand in de schrijfmodus ('w' staat voor write)
with open(bestandsnaam, 'w') as bestand:
    # Voeg tekst toe aan het bestand
    bestand.write("Dit is mijn eerste regel tekst.\n")
    bestand.write("Dit is de tweede regel tekst.\n")
    bestand.write("Nog een regel tekst voor de oefening.\n")

print(f"Het bestand '{bestandsnaam}' is succesvol aangemaakt en bijgewerkt.")
