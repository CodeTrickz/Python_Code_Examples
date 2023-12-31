from flask import Flask, render_template

app = Flask(__name__)

# Voorbeeldgegevens
gebruikers = [
    {'id': 1, 'naam': 'John', 'leeftijd': 28},
    {'id': 2, 'naam': 'Jane', 'leeftijd': 24},
    {'id': 3, 'naam': 'Doe', 'leeftijd': 32}
]


@app.route('/')
def index():
    return render_template('index.html', gebruikers=gebruikers)


@app.route('/gebruiker/<identifier>')
def gebruiker(identifier):
    try:
        # Probeer eerst te zoeken op ID
        gebruiker = next(
            (u for u in gebruikers if u['id'] == int(identifier)), None)
    except ValueError:
        gebruiker = None

    # Als zoeken op ID mislukt, probeer dan te zoeken op naam
    if gebruiker is None:
        gebruiker = next(
            (u for u in gebruikers if u['naam'].lower() == identifier.lower()), None)

    if gebruiker:
        return render_template('gebruiker.html', gebruiker=gebruiker)
    else:
        return render_template('gebruiker_niet_gevonden.html')


if __name__ == '__main__':
    app.run(debug=True)


if __name__ == '__main__':
    app.run(debug=True)
