import requests

# Vervang de onderstaande Pokemon-naam door de naam van de Pokemon die je zoekt
pokemon_name = "ditto"

# URL van de PokeAPI voor het zoeken naar een Pokemon op basis van de naam
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

# Doe een GET-verzoek naar de URL
response = requests.get(url)

# Controleer of het verzoek succesvol was (statuscode 200)
if response.status_code == 200:
    # Probeer de JSON-gegevens van het antwoord te laden
    try:
        pokemon_data = response.json()

        # Print enkele informatie over de gevonden Pokemon
        print("Naam:", pokemon_data["name"])
        print("Hoogte:", pokemon_data["height"])
        print("Gewicht:", pokemon_data["weight"])
        print("Type(s):", [t["type"]["name"] for t in pokemon_data["types"]])
    except ValueError:
        print("Fout bij het laden van JSON-gegevens.")
else:
    # Toon een foutmelding als het verzoek niet succesvol was
    print(
        f"Fout bij het doen van het verzoek. Statuscode: {response.status_code}")
