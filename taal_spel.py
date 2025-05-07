import random
import pyttsx3

woordenlijst = {
    'hond': ['chien', 'Hund', 'dog'],
    'kat': ['chat', 'Katze', 'cat'],
    'huis': ['maison', 'Haus', 'house'],
    'auto': ['voiture', 'Auto', 'car'],
}

def spreek_uit(woord):
    engine = pyttsx3.init()
    engine.say(woord)
    engine.runAndWait()

def start_spel():
    print("Welkom bij het vertaalspel!")
    taal_keuze = input("Kies een taal om te leren (frans, duits, engels): ").lower()

    while True:
        nederlands_woord = random.choice(list(woordenlijst.keys()))
        vertalingen = woordenlijst[nederlands_woord]

        if taal_keuze == 'frans':
            vertaal_woord = vertalingen[0]
        elif taal_keuze == 'duits':
            vertaal_woord = vertalingen[1]
        elif taal_keuze == 'engels':
            vertaal_woord = vertalingen[2]
        else:
            print("Ongeldige keuze.")
            continue

        print(f"Vertaal: {nederlands_woord} naar {taal_keuze}")
        spreek_uit(vertaal_woord)

        antwoord = input("Jouw antwoord: ").lower()

        if antwoord == vertaal_woord:
            print("✅ Goed gedaan!")
        else:
            print(f"❌ Fout. Het juiste antwoord is: {vertaal_woord}")

start_spel()
