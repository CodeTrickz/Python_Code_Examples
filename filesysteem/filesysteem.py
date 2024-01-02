import os


def zoek_bestanden(map_pad):
    for mapnaam, mappen, bestanden in os.walk(map_pad):
        print(f"Map: {mapnaam}")
        for bestand in bestanden:
            print(f"  Bestand: {bestand}")


def zoek_bestanden_met_extensies(map_pad, extensies):
    gevonden_bestanden = []
    for mapnaam, mappen, bestanden in os.walk(map_pad):
        for bestand in bestanden:
            if any(bestand.endswith(extensie) for extensie in extensies):
                gevonden_bestanden.append(os.path.join(mapnaam, bestand))

    return gevonden_bestanden


# Voorbeeldgebruik: geef het pad van het startpunt op
start_map = ".."
gewenste_extensies = [".txt", ".pdf", ".docx", ".html"]

zoek_bestanden(start_map)

gevonden_bestanden = zoek_bestanden_met_extensies(
    start_map, gewenste_extensies)

if gevonden_bestanden:
    print(f"Gevonden bestanden met de extensie '{gewenste_extensies}':")
    for bestand in gevonden_bestanden:
        print(bestand)
else:
    print(f"Geen bestanden gevonden met de extensie '{gewenste_extensies}'.")
