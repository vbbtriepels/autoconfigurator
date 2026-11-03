import sys

basisprijs = 7500
prijs = 7500
attr_namen = ["model", "motor", "kleur", "uitvoering", "merk", "accessoires"]
attr_prijs = []

# maak dictionaries met de naam van het attribuut samen met de prijs
attr_model = {
    "a1": 0,
    "a2": 200,
    "a3": 300,
    "a4": 400,
    "a5": 500
}
attr_motor = {
    "v3": 0,
    "v5": 100,
    "v6": 200,
    "v8": 300,
    "v10": 400,
    "v12": 500
}
attr_kleur = {
    "zilvergrijs": 0,
    "nardogrijs": 100,
    "wit": 200,
    "zwart": 300,
    "blauw": 325,
    "roze": 350,
    "rood": 400,
    "geel": 600
}
attr_uitvoering = {
    "hatchback": 0,
    "sedan": 200,
    "stationwagen": 300,
    "cabriolet": 400,
    "spyder": 500
}
attr_merk = {
    "fiat": 0,
    "nissan": 200,
    "jeep": 300,
    "mini": 400,
    "audi": 500,
    "bmw": 600,
    "mercedes": 700,
    "range rover": 800,
    "porsche": 1000
}
attr_acc = {
    "geen": 0,
    "dobbelstenen": 5,
    "bumpersticker": 10,
    "bobbelhead": 15,
    "wimpers": 20,
    "stuurbekleding": 25,
    "stoelbekleding": 75,
    "stoelverwarming": 150,
    "carbon pakket": 200
}

# Hoofdmenu
print("\n---------- Welkom bij onze Auto-Configurator! ----------")

# print 1 lege lijn zodat het mooier is
print()

creeer = input("Wilt u een nieuwe auto samenstellen (ja/nee): ").lower()

if creeer in ("ja", "j"):

    print("\n\nMerken: ")

    for i, j in attr_merk.items():
        print(" -" + i.title(), f"\n    Prijs: €{j}")
    merk = input("Welk model wilt u hebben: ").lower()

    prijs += attr_merk.get(merk)

    attr_prijs.append(attr_merk.get(merk))

    # vraag de gebruiker voor welk model
    print("\n\nModellen: ")

    # deze for loop blijft net zo vaak herhalen als dat er dingen staan in de lijsten
    # dit wordt gedaan om de gebruiker een overzicht te geven over welke opties 
    # de gebruiker heeft
    for i, j in attr_model.items():
        print(" -" + i.capitalize(), f"\n    Prijs: €{j}")
    model = input("Welk model wilt u hebben: ").lower()

    # omdat er een dictionary is gebruikt moet de .get() methode 
    # gebruikt worden om de waardes te krijgen
    # prijs += 10 
    # prijs = prijs + 10
    prijs += attr_model.get(model)

    # voeg de prijs van het model toe aan de lijst attr_prijs
    attr_prijs.append(attr_model.get(model))

    # vraag de gebruiker voor welke motor
    print("\n\nMotoren: ")

    # deze for loop blijft net zo vaak herhalen als dat er dingen staan in de lijsten
    # dit wordt gedaan om de gebruiker een overzicht te geven over welke opties 
    # de gebruiker heeft
    for i, j in attr_motor.items():
        print(" -" + i.capitalize(), f"\n    Prijs: €{j}")
    motor = input("Welke motor wilt u hebben: ").lower()

    # omdat er een dictionary is gebruikt moet de .get() methode 
    # gebruikt worden om de waardes te krijgen
    prijs += attr_motor.get(motor)

    # voeg de prijs van de motor toe aan de lijst attr_prijs
    attr_prijs.append(attr_motor.get(motor))

    # vraag de gebruiker voor welke kleur
    print("\n\nKleuren: ")

    # deze for loop blijft net zo vaak herhalen als dat er dingen staan in de lijsten
    # dit wordt gedaan om de gebruiker een overzicht te geven over welke opties 
    # de gebruiker heeft
    for i, j in attr_kleur.items():
        print(" -" + i.capitalize(), f"\n    Prijs: €{j}")
    kleur = input("Welke kleur wilt u hebben: ").lower()

    # omdat er een dictionary is gebruikt moet de .get() methode 
    # gebruikt worden om de waardes te krijgen
    prijs += attr_kleur.get(kleur)

    # voeg de prijs van de kleur toe aan de lijst attr_prijs
    attr_prijs.append(attr_kleur.get(kleur))

    print("\n\nAccessoires: ")

    for i, j in attr_acc.items():
        print(" -" + i.capitalize(), f"\n    Prijs: €{j}")
    acc = input("Welke accessoire wilt u hebben: ").lower()

    prijs += attr_acc.get(acc)

    attr_prijs.append(attr_acc.get(acc))

    # vraag de gebruiker voor welke uitvoering
    print("\n\nUitvoeringen: ")

    # deze for loop blijft net zo vaak herhalen als dat er dingen staan in de lijsten
    # dit wordt gedaan om de gebruiker een overzicht te geven over welke opties 
    # de gebruiker heeft
    for i, j in attr_uitvoering.items():
        print(" -" + i.capitalize(), f"\n    Prijs: €{j}")
    uitvoering = input("Welke uitvoering wilt u hebben: ").lower()

    # omdat er een dictionary is gebruikt moet de .get() methode 
    # gebruikt worden om de waardes te krijgen
    prijs += attr_uitvoering.get(uitvoering)

    # voeg de prijs van de uitvoering toe aan de lijst attr_prijs
    attr_prijs.append(attr_uitvoering.get(uitvoering))

    # opent de file autos.txt en indien hij niet bestaat maakt hij het bestand aan
    attr_waardes = [merk, model, motor, kleur, acc, uitvoering]
    with open("autos.txt", "a") as file:
        file.write("\nAuto:\n")

        # zip(..., ...) voegt de lijsten attr_namen en attr_waardes zodat 
        # elke item uit lijst 1 gepaard wordt met het 'corresponding' item uit lijst 2

        # voorbeeld:
        # lijst1 = [1, 2, 3]
        # lijst2 = [4, 5, 6]
        # print(list(zip(lijst1, lijst2)))
        # dit geeft "[(1, 4), (2, 5), (3, 6)]"
        # dus '1' uit lijst 1 is gepaard met '4' uit lijst twee, beide de eerste item uit de lijsten

        # VOOR REFERENTIE KIJK IN zipdemo.py

        # dit wordt gedaan zodat het programma makkelijker is bij te werken met meer waardes
        for i, j in zip(attr_namen, attr_waardes):
            # geeft de eerste waarde uit de eerste tuple in de gezipte lijst en hoofdletter't hem
            file.write(f" -{i.capitalize()}: ")

            # schrijf vervolgens de waarde van het attribuut meteen achter de vorige lijn aan
            file.write(j.title())

            # schrijft een 'new-line' character om het overzichtelijker te maken
            file.write("\n")
        file.write(f" -Prijs: {"€" + str(prijs)}\n")

        # schrijft na alle naam, waarde combos nóg een new-line character om de volgende auto
        # mooier neer te zetten in het bestand
        file.write("\n")

    # toont alle resultaten aan de gebruiker, NADAT het allemaal is opgeslagen in het bestand
    print("\n\nUw auto:")
    print(f"-Basisprijs {basisprijs}")
    for i, j, k in zip(attr_namen, attr_waardes, attr_prijs):
        print(f" -{i.capitalize()}: ", j.title(), "   +€" + str(k), sep="")
    print(f"\nPrijs: {prijs}")
    print("\n")

# als de gebruiker geen nieuwe auto wilt maken
elif creeer in ("nee", "n"):
    showON = input("Wilt u alle andere auto's inzien (ja/nee): ")
    if showON in ("ja", "j"):
        with open("autos.txt", "r") as file:
            print(file.read())
    else:
        print("Bedankt voor het Auto-Configurator programma gebruiken!")

        # sys.exit() sluit het programma zodat de print() statement aan het einde niet ook
        # 'Bedankt voor het Auto-Configurator programma gebruiken!' print
        sys.exit()

# als er iets fout is gegaan, dus als de gebruiker geen ('j' of 'ja') of ('n' of 'nee') typte
# of iets anders typte
else:
    print("Er is iets fout gegaan, programma wordt afgesloten.")
    sys.exit()

# laatste afscheidsbericht printen voor de gebruiker indien nodig
print("Bedankt voor het Auto-Configurator programma gebruiken!")