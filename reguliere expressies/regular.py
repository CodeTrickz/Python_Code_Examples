import re

# Voorbeeldtekst
tekst = """
E-mail: voorbeeld@email.com
Telefoon: +31 123 456 789
Datum: 01-01-2022
IP-adres: 192.168.1.1
URL: https://www.example.com
"""

# Regelmatige expressies
email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
# # \b: Woordgrens.
# [A-Za-z0-9._%+-]+: Een of meer letters, cijfers, punten, underscores, procenttekens, plustekens en streepjes.
# @: Het at-teken.
# [A-Za-z0-9.-]+: Een of meer letters, cijfers, punten en streepjes.
# \.: Het punt na het domeingedeelte.
# [A-Z|a-z]{2,}: Twee of meer letters voor het domeingedeelte (top-level domein, zoals com, org, nl, etc.).
# \b: Woordgrens.
telefoon_regex = r'\+\d{2,3}\s\d{3}\s\d{3}\s\d{3}'
# \+: Het plusteken.
# \d{2,3}: Twee of drie cijfers voor de landcode.
# \s: Een spatie.
# \d{3}: Drie cijfers voor het netnummer.
# \s: Een spatie.
# \d{3}: Drie cijfers voor het eerste deel van het telefoonnummer.
# \s: Een spatie.
# \d{3}: Drie cijfers voor het tweede deel van het telefoonnummer.
datum_regex = r'\d{2}-\d{2}-\d{4}'
# \d{2}: Twee cijfers voor de dag.
# -: Het streepje als scheidingsteken.
# \d{2}: Twee cijfers voor de maand.
# -: Het streepje als scheidingsteken.
# \d{4}: Vier cijfers voor het jaar.
ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
# \b: Woordgrens.
# (?:\d{1,3}\.){3}: Drie groepen van één tot drie cijfers, gescheiden door punten (niet-capturende groep met (?:...)).
# \d{1,3}: Een groep van één tot drie cijfers.
# \b: Woordgrens.
url_regex = r'https?://\S+'
# https?: "http" gevolgd door een optionele "s" voor HTTPS.
# ://: De dubbelepunt-slash-slash die volgt op "http" of "https".
# \S+: Eén of meer niet-spatietekens, wat de rest van de URL vertegenwoordigt.

# Zoek naar overeenkomsten met reguliere expressies
email_match = re.search(email_regex, tekst)
telefoon_match = re.search(telefoon_regex, tekst)
datum_match = re.search(datum_regex, tekst)
ip_match = re.search(ip_regex, tekst)
url_match = re.search(url_regex, tekst)

# Geef resultaten weer
print("E-mail:", email_match.group()
      if email_match else "Geen overeenkomst gevonden")
print("Telefoon:", telefoon_match.group()
      if telefoon_match else "Geen overeenkomst gevonden")
print("Datum:", datum_match.group()
      if datum_match else "Geen overeenkomst gevonden")
print("IP-adres:", ip_match.group() if ip_match else "Geen overeenkomst gevonden")
print("URL:", url_match.group() if url_match else "Geen overeenkomst gevonden")
