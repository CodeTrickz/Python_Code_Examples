import csv
import json

# Functie om gegevens uit een CSV-bestand te halen


def lees_csv_bestand(bestandsnaam):
    data = []
    with open(bestandsnaam, newline='') as csvfile:
        lezer = csv.DictReader(csvfile)
        for rij in lezer:
            data.append(rij)
    return data

# Functie om gegevens uit een JSON-bestand te halen


def lees_json_bestand(bestandsnaam):
    with open(bestandsnaam, 'r') as jsonfile:
        data = json.load(jsonfile)
    return data["studenten"]

# Functie om een specifiek element uit CSV-gegevens te halen


def haal_specifiek_element_csv(csv_gegevens, naam):
    for student in csv_gegevens:
        if student['Naam'] == naam:
            return student
    return None

# Functie om een specifiek element uit JSON-gegevens te halen


def haal_specifiek_element_json(json_gegevens, naam):
    for student in json_gegevens:
        if student['naam'] == naam:
            return student
    return None


# Voorbeeldgebruik
csv_gegevens = lees_csv_bestand('example.csv')
json_gegevens = lees_json_bestand('example.json')

# Weergave van gegevens uit CSV-bestand
print("Gegevens uit CSV-bestand:")
for student in csv_gegevens:
    print(student)

print("\n")

# Weergave van gegevens uit JSON-bestand
print("Gegevens uit JSON-bestand:")
for student in json_gegevens:
    print(student)

print("\n")

# Voorbeeld van het gebruik van de functie om een specifiek element op te halen
specifieke_naam = 'Eva de Vries'
csv_student = haal_specifiek_element_csv(csv_gegevens, specifieke_naam)
json_student = haal_specifiek_element_json(json_gegevens, specifieke_naam)

print(
    f"Specifieke gegevens voor {specifieke_naam} uit CSV-bestand: {csv_student}")
print(
    f"Specifieke gegevens voor {specifieke_naam} uit JSON-bestand: {json_student}")
