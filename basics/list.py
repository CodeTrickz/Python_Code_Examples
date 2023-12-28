# Een lijst met namen van studenten
studenten_namen = ['Jan Jansen', 'Eva de Vries', 'Piet Petersen']

# Weergave van alle studenten in de lijst
print("Alle studenten:")
for naam in studenten_namen:
    print(naam)

# Toevoegen van een nieuwe student aan de lijst
nieuwe_student = 'Lisa de Boer'
studenten_namen.append(nieuwe_student)

# Weergave van de bijgewerkte lijst met studenten
print("\nLijst na toevoeging van nieuwe student:")
for naam in studenten_namen:
    print(naam)
